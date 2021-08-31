import sys
import os

from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

from . import components_widget
from . import canvas_widget
from . import management_widget
from . import options_widget

from cvlab import constants


class MainWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 

        # Define the icon
        self.setWindowIcon(QtGui.QIcon(
            os.path.join(os.path.dirname(__file__), 
                         constants.ICON_RELATIVE_PATH)))
        
        # Set the title 
        self.setWindowTitle(constants.MAIN_WINDOW_TITLE) 

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

        self.components_widget.setSizePolicy(
            QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.canvas_widget.setSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.management_widget.setSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.options_widget.setSizePolicy(
            QSizePolicy.Maximum, QSizePolicy.Maximum)

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