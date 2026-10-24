from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from sorters.catalog import ALLLABELS
from bench.config import KINDNAMES

BG = '#1b1b1f'
PLOTBG = '#222228'
TEXT = '#e6e6e6'
LINECOLORS = ['#ff9f43', '#54a0ff', '#1dd1a1', '#ff6b6b',
              '#feca57', '#c8d6e5', '#a29bfe', '#fd79a8']


class ChartPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.summary = []

        top = QHBoxLayout()
        top.addWidget(QLabel('Input type:'))
        self.kindCombo = QComboBox()
        self.kindCombo.setMinimumWidth(220)
        self.kindCombo.currentTextChanged.connect(self.draw)
        top.addWidget(self.kindCombo)
        top.addStretch(1)

        self.figure = Figure(facecolor=BG)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)

        layout = QVBoxLayout(self)
        layout.addLayout(top)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas, 1)
        self.draw('')

    def setData(self, summary):
        self.summary = summary
        kinds = []
        for row in summary:
            if row['kind'] not in kinds:
                kinds.append(row['kind'])
        self.kindCombo.blockSignals(True)
        self.kindCombo.clear()
        for kind in kinds:
            self.kindCombo.addItem(KINDNAMES[kind], kind)
        self.kindCombo.blockSignals(False)
        self.draw(self.kindCombo.currentData())

    def draw(self, kindName):
        kind = self.kindCombo.currentData()
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor(PLOTBG)
        for spine in ax.spines.values():
            spine.set_color('#555560')
        ax.tick_params(colors='#cccccc', labelsize=13)

        drawn = False
        for label in ALLLABELS:
            points = [r for r in self.summary if r['label'] == label and r['kind'] == kind]
            points.sort(key=lambda r: r['size'])
            if len(points) > 0:
                colour = LINECOLORS[ALLLABELS.index(label) % len(LINECOLORS)]
                ax.plot([p['size'] for p in points], [p['median'] for p in points],
                        marker='o', linewidth=2.5, markersize=8, color=colour,
                        label=points[0]['name'])
                drawn = True

        if drawn:
            ax.set_xscale('log')
            ax.set_yscale('log')
            ax.set_title('Median sort time: ' + KINDNAMES.get(kind, ''), color=TEXT, fontsize=18)
            ax.set_xlabel('Array size', color='#cccccc', fontsize=15)
            ax.set_ylabel('Median time (ms)', color='#cccccc', fontsize=15)
            ax.grid(True, linestyle=':', alpha=0.35)
            legend = ax.legend(facecolor='#2b2b33', edgecolor='#555560', fontsize=13)
            for text in legend.get_texts():
                text.set_color(TEXT)
        else:
            ax.text(0.5, 0.5, 'Run a benchmark to see the chart', ha='center',
                    va='center', color='#888888', fontsize=18, transform=ax.transAxes)
            ax.set_xticks([])
            ax.set_yticks([])
        self.canvas.draw()