import sys

from PyQt5.QtWidgets import * 


class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 

        # set the title 
        self.setWindowTitle("Hello World!") 

        # set the geometry 
        self.setGeometry(0, 0, 300, 300) 

        # create label widget 
        # to display content on screen 
        self.label = QLabel("Hello World !!", self) 

        # show all the widgets 
        self.show() 


def run_main_window():
    """Everything it is needed for launching the main window"""

    # create pyqt5 app 
    App = QApplication(sys.argv) 

    # create the instance of our Window 
    window = MainWindow() 

    # start the app 
    sys.exit(App.exec()) 