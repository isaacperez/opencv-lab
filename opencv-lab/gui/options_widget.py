from PyQt5.QtWidgets import *


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.options_label = QLabel("Options layout")
        self.layout.addWidget(self.options_label)

        self.setStyleSheet("background-color: green; border: 1px solid black;")
            
            