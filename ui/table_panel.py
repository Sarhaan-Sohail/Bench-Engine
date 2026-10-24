from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from bench.config import KINDNAMES


class TablePanel(QTableWidget):
    def __init__(self):
        super().__init__(0, 7)
        self.setHorizontalHeaderLabels(
            ['Algorithm', 'Input type', 'Size', 'Median (ms)', 'Min (ms)', 'Comparisons', 'Swaps'])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setEditTriggers(QTableWidget.NoEditTriggers)

    def fill(self, summary):
        self.setSortingEnabled(False)
        self.setRowCount(len(summary))
        for r in range(len(summary)):
            row = summary[r]
            values = [row['name'], KINDNAMES.get(row['kind'], row['kind']), row['size'],
                      round(row['median'], 4), round(row['min'], 4),
                      row['comparisons'], row['swaps']]
            for c in range(len(values)):
                item = QTableWidgetItem()
                item.setData(Qt.DisplayRole, values[c])
                self.setItem(r, c, item)
        self.setSortingEnabled(True)