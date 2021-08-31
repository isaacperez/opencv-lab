from PyQt5.QtWidgets import *


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.components_label = QLabel("Components layout")
        self.layout.addWidget(self.components_label)

        self.setStyleSheet("background-color: yellow; border: 1px solid black;")
            
            