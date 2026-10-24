import datetime
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QSplitter,
                             QPushButton, QLabel, QProgressBar, QTabWidget, QMessageBox)

from bench.storage import writeruns, writecounts, writemetadata
from bench.summary import buildSummary
from ui.algorithm_panel import AlgorithmTree
from ui.settings_panel import SettingsPanel
from ui.chart_panel import ChartPanel
from ui.table_panel import TablePanel
from ui.run_worker import RunWorker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Bench Engine')
        self.setMinimumSize(1200, 800)
        self.worker = None
        self.runRows = []
        self.countRows = []
        self.summary = []
        self.lastSettings = {}

        self.algorithmTree = AlgorithmTree()
        self.settings = SettingsPanel()
        self.chartPanel = ChartPanel()
        self.tablePanel = TablePanel()

        self.runButton = QPushButton('Run benchmark')
        self.runButton.setObjectName('runbutton')
        self.runButton.clicked.connect(self.startRun)

        self.stopButton = QPushButton('Stop')
        self.stopButton.setEnabled(False)
        self.stopButton.clicked.connect(self.stopRun)

        self.saveButton = QPushButton('Save results (CSV)')
        self.saveButton.setEnabled(False)
        self.saveButton.clicked.connect(self.saveResults)

        self.progressBar = QProgressBar()
        self.statusLabel = QLabel('Ready. Pick algorithms and settings, then press Run benchmark.')
        self.statusLabel.setWordWrap(True)

        left = QWidget()
        leftLayout = QVBoxLayout(left)
        heading = QLabel('Algorithms')
        heading.setObjectName('heading')
        leftLayout.addWidget(heading)
        leftLayout.addWidget(self.algorithmTree, 1)
        leftLayout.addWidget(self.settings)
        leftLayout.addWidget(self.runButton)
        leftLayout.addWidget(self.stopButton)
        leftLayout.addWidget(self.saveButton)
        leftLayout.addWidget(self.progressBar)
        leftLayout.addWidget(self.statusLabel)

        tabs = QTabWidget()
        tabs.addTab(self.chartPanel, 'Chart')
        tabs.addTab(self.tablePanel, 'Table')

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left)
        splitter.addWidget(tabs)
        splitter.setSizes([460, 1000])
        self.setCentralWidget(splitter)

    def startRun(self):
        labels = self.algorithmTree.selectedLabels()
        kinds = self.settings.checkedKinds()
        sizes = self.settings.checkedSizes()

        if len(labels) == 0 or len(kinds) == 0 or len(sizes) == 0:
            QMessageBox.warning(self, 'Nothing selected',
                                'Pick at least one algorithm, one input type and one size.')
            return

        warmups = self.settings.warmupSpin.value()
        repeats = self.settings.repeatSpin.value()
        seed = self.settings.seedSpin.value()
        skipSlow = self.settings.skipSlowCheck.isChecked()

        self.lastSettings = {
            'labels': labels, 'kinds': kinds, 'sizes': sizes,
            'warmups': warmups, 'repeats': repeats, 'seed': seed,
            'skip_slow_above_5000': skipSlow, 'started_from': 'app.py',
        }

        self.worker = RunWorker(labels, kinds, sizes, warmups, repeats, seed, skipSlow)
        self.worker.progress.connect(self.onProgress)
        self.worker.done.connect(self.onDone)
        self.runButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.saveButton.setEnabled(False)
        self.progressBar.setValue(0)
        self.worker.start()

    def stopRun(self):
        if self.worker is not None:
            self.worker.stopRequested = True
            self.statusLabel.setText('Stopping after the current sort...')

    def onProgress(self, finished, total, text):
        if total > 0:
            self.progressBar.setValue(int(100 * finished / total))
        self.statusLabel.setText(text)

    def onDone(self, runRows, countRows):
        self.runRows = runRows
        self.countRows = countRows
        self.summary = buildSummary(runRows, countRows)
        self.tablePanel.fill(self.summary)
        self.chartPanel.setData(self.summary)
        self.runButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.saveButton.setEnabled(len(runRows) > 0)

    def saveResults(self):
        os.makedirs('results', exist_ok=True)
        stamp = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
        writeruns('results/ui_runs_' + stamp + '.csv', self.runRows)
        writecounts('results/ui_counts_' + stamp + '.csv', self.countRows)
        writemetadata('results/ui_meta_' + stamp + '.json', self.lastSettings)
        self.statusLabel.setText('Saved 3 files in the results folder (ui_..._' + stamp + ')')