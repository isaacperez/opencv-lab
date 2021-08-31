from PyQt5.QtWidgets import *


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)


        self.components_list = QListWidget()
        #self.components_list.setResizeMode(QListView.Fixed)


        self.components_list.addItems(['Winnie Puh', 'Monday', 'Tuesday', 'Minnesota', 'Dracula Calista Flockhart Meningitis', 'Once', '123345', 'Fin'])
        #self.components_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.components_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.components_list.setFixedSize(self.components_list.sizeHintForColumn(0) + 2 * self.components_list.frameWidth(), self.components_list.sizeHintForRow(0) * self.components_list.count() + 2 * self.components_list.frameWidth())



        self.layout.addWidget(self.components_list)


        self.setStyleSheet("background-color: green; border: 1px solid black;")
            
            