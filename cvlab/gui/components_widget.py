from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.top_label = QLabel("OpenCV modules")


        self.components_list = QToolBox()
        

        self.components_list.addItem(QWidget(), 'core')
        self.components_list.addItem(QWidget(), 'imgproc')
        self.components_list.addItem(QWidget(), 'imgcodecs')


        self.layout.addWidget(self.top_label)
        self.layout.addWidget(self.components_list)

        self.setStyleSheet("background-color: yellow; border: 1px solid black;")
            
        