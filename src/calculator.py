"""
a calculator program
- from chapter 4 of book
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class MainWidget(QDialog):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.browser)
        self.layout.addWidget(self.lineedit)
        self.setLayout(self.layout)

        self.setWindowTitle("Calculate")

    def updateUi(self):
        self.browser.append(f"<font color=red>{self.lineedit.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    app.exec_()
