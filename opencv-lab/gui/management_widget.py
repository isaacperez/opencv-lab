from PyQt5.QtWidgets import *


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.management_label = QLabel("Management layout")
        self.layout.addWidget(self.management_label)

        self.setStyleSheet("background-color: blue; border: 1px solid black;")
            
            