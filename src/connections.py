"""
a signal/slots program
- from chapter 4 of book
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class MainWidget(QDialog):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.button1 = QPushButton("One")
        self.button1.clicked.connect(self.onButton1Clicked)
        self.button2 = QPushButton("Two")
        self.button2.clicked.connect(self.onButton2Clicked)
        self.button3 = QPushButton("Three")
        self.button3.clicked.connect(self.onButton3Clicked)
        self.button4 = QPushButton("Four")
        self.button4.clicked.connect(self.onButton4Clicked)
        self.button5 = QPushButton("Five")
        self.button5.clicked.connect(self.onButton5Clicked)
        self.label = QLabel("Click a button...")

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5)
        self.layout.addStretch()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.setWindowTitle("Connections")

    def onButton1Clicked(self):
        self.label.setText(f"You clicked button 'One'")

    def onButton2Clicked(self):
        self.label.setText(f"You clicked button 'Two'")

    def onButton3Clicked(self):
        self.label.setText(f"You clicked button 'Three'")

    def onButton4Clicked(self):
        self.label.setText(f"You clicked button 'Four'")

    def onButton5Clicked(self):
        self.label.setText(f"You clicked button 'Five'")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    app.exec_()
