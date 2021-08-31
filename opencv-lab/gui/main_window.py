import sys

from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

from . import components_widget
from . import canvas_widget
from . import management_widget
from . import options_widget


class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 

        # Set the title 
        self.setWindowTitle("Hello World!") 

        # Create a central widget and set it as a central widget for the 
        # main window
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a QGridLayout instance
        self.top_layout = QGridLayout()

        # Add the widgets to the top layout
        self.components_widget = components_widget.Widget()
        self.canvas_widget = canvas_widget.Widget()
        self.management_widget = management_widget.Widget()
        self.options_widget = options_widget.Widget()

        self.top_layout.addWidget(self.components_widget, 0, 0, 4, 1)
        self.top_layout.addWidget(self.canvas_widget, 0, 1, 3, 4)
        self.top_layout.addWidget(self.management_widget, 3, 1, 1, 5)
        self.top_layout.addWidget(self.options_widget, 0, 5, 3, 1)

        # Set the layout on the application's window
        self.central_widget.setLayout(self.top_layout)

        # Show the application maximized
        self.showMaximized()


def run_main_window():
    """Everything it is needed for launching the main window"""

    # Create pyqt5 app 
    App = QApplication(sys.argv) 

    # Create the instance of our Window 
    window = MainWindow() 

    # Start the app 
    sys.exit(App.exec()) 