import sys
from PyQt5.QtWidgets import QApplication
from ui.theme import STYLE
from ui.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())