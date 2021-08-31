from PyQt5.QtWidgets import *


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.canvas_label = QLabel("Canvas layout")
        self.layout.addWidget(self.canvas_label)

        self.setStyleSheet("background-color: red; border: 1px solid black;")
            
            