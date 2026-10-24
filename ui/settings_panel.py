from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QGroupBox, QCheckBox, QLabel, QSpinBox)
from bench.config import KINDS, KINDNAMES, ALLSIZES, DEFAULTSIZES


class SettingsPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # input types and sizes side by side
        pickRow = QHBoxLayout()

        kindBox = QGroupBox('Input types')
        kindLayout = QVBoxLayout(kindBox)
        self.kindChecks = {}
        for kind in KINDS:
            check = QCheckBox(KINDNAMES[kind])
            check.setChecked(True)
            kindLayout.addWidget(check)
            self.kindChecks[kind] = check
        pickRow.addWidget(kindBox)

        sizeBox = QGroupBox('Sizes')
        sizeGrid = QGridLayout(sizeBox)
        self.sizeChecks = {}
        for index in range(len(ALLSIZES)):
            size = ALLSIZES[index]
            check = QCheckBox(str(size))
            check.setChecked(size in DEFAULTSIZES)
            sizeGrid.addWidget(check, index // 2, index % 2)
            self.sizeChecks[size] = check
        pickRow.addWidget(sizeBox)
        layout.addLayout(pickRow)

        # number settings
        numberBox = QGroupBox('Settings')
        numberLayout = QVBoxLayout(numberBox)
        self.repeatSpin = self.makeSpin(1, 50, 7)
        self.warmupSpin = self.makeSpin(0, 10, 2)
        self.seedSpin = self.makeSpin(0, 99999, 42)
        for label, spin in [('Repeats', self.repeatSpin),
                            ('Warm-ups', self.warmupSpin),
                            ('Seed', self.seedSpin)]:
            row = QHBoxLayout()
            row.addWidget(QLabel(label))
            row.addStretch(1)
            row.addWidget(spin)
            numberLayout.addLayout(row)

        self.skipSlowCheck = QCheckBox('Skip slow ones above 5000')
        self.skipSlowCheck.setChecked(True)
        numberLayout.addWidget(self.skipSlowCheck)
        layout.addWidget(numberBox)

    def makeSpin(self, low, high, value):
        spin = QSpinBox()
        spin.setRange(low, high)
        spin.setValue(value)
        spin.setMinimumWidth(110)
        return spin

    def checkedKinds(self):
        return [kind for kind in KINDS if self.kindChecks[kind].isChecked()]

    def checkedSizes(self):
        return [size for size in ALLSIZES if self.sizeChecks[size].isChecked()]