STYLE = """
QWidget { background-color: #1b1b1f; color: #e6e6e6; font-size: 16px; }
QLabel#heading { color: #ff9f43; font-size: 20px; font-weight: bold; }
QGroupBox { border: 1px solid #3a3a42; border-radius: 8px; margin-top: 14px; padding-top: 10px; font-size: 16px; }
QGroupBox::title { subcontrol-origin: margin; left: 12px; color: #ff9f43; }
QTreeWidget { background-color: #222228; border: 1px solid #3a3a42; border-radius: 6px; font-size: 17px; }
QTreeWidget::item { padding: 5px; }
QTreeWidget::indicator, QCheckBox::indicator { width: 18px; height: 18px; border: 1px solid #77777f; border-radius: 4px; background: #222228; }
QTreeWidget::indicator:checked, QCheckBox::indicator:checked { background: #ff9f43; border: 1px solid #ff9f43; }
QTreeWidget::indicator:indeterminate { background: #7a5a33; border: 1px solid #ff9f43; }
QCheckBox { spacing: 8px; padding: 3px; }
QPushButton { background-color: #2b2b33; border: 1px solid #44444d; border-radius: 6px; padding: 10px; font-size: 17px; }
QPushButton:hover { background-color: #36363f; }
QPushButton:disabled { color: #777; }
QPushButton#runbutton { background-color: #ff9f43; color: #1b1b1f; font-weight: bold; border: none; }
QPushButton#runbutton:disabled { background-color: #6b5230; color: #1b1b1f; }
QSpinBox, QComboBox { background-color: #2b2b33; border: 1px solid #44444d; border-radius: 5px; padding: 5px; font-size: 16px; min-height: 26px; }
QProgressBar { border: 1px solid #44444d; border-radius: 5px; text-align: center; background-color: #2b2b33; height: 24px; font-size: 15px; }
QProgressBar::chunk { background-color: #ff9f43; border-radius: 4px; }
QTableWidget { background-color: #222228; gridline-color: #34343c; font-size: 16px; }
QHeaderView::section { background-color: #2b2b33; padding: 8px; border: none; font-size: 16px; font-weight: bold; }
QTabBar::tab { background: #2b2b33; padding: 12px 28px; font-size: 17px; border-top-left-radius: 6px; border-top-right-radius: 6px; }
QTabBar::tab:selected { background: #ff9f43; color: #1b1b1f; font-weight: bold; }
QTabWidget::pane { border: 1px solid #3a3a42; border-radius: 6px; }
"""