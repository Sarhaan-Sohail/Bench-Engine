from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from sorters.catalog import GROUPS


class AlgorithmTree(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setHeaderHidden(True)
        self.setMinimumHeight(260)

        for groupName, options in GROUPS:
            if len(options) == 1 and options[0][0] == '':
                item = QTreeWidgetItem([groupName])
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                item.setData(0, Qt.UserRole, options[0][1])
                item.setCheckState(0, Qt.Checked)
                self.addTopLevelItem(item)
            else:
                parent = QTreeWidgetItem([groupName])
                parent.setFlags(parent.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsAutoTristate)
                self.addTopLevelItem(parent)
                for optionName, optionLabel in options:
                    child = QTreeWidgetItem([optionName])
                    child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                    child.setData(0, Qt.UserRole, optionLabel)
                    parent.addChild(child)
                parent.setCheckState(0, Qt.Checked)
                parent.setExpanded(True)

    def selectedLabels(self):
        labels = []
        for i in range(self.topLevelItemCount()):
            top = self.topLevelItem(i)
            if top.childCount() == 0:
                if top.checkState(0) == Qt.Checked:
                    labels.append(top.data(0, Qt.UserRole))
            else:
                for j in range(top.childCount()):
                    child = top.child(j)
                    if child.checkState(0) == Qt.Checked:
                        labels.append(child.data(0, Qt.UserRole))
        return labels