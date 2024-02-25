import sys
from PySide6.QtWidgets import QSplitter, QWidget, QMainWindow, QVBoxLayout
from PySide6.QtCore import Qt
from gui.sideBar.sidebar import SideBar
from gui.workspace.workspace import DropArea

class App(QMainWindow):
    def __init__(self, settings):
        super().__init__()
        self.setWindowTitle("VisionTaskFlow")
        self.setGeometry(100, 100, 800, 600)

        # Create the splitter
        splitter = QSplitter(Qt.Horizontal)

        # Create two text edit widgets and add them to the splitter
        sideBar = SideBar(settings)
        workspace = DropArea()
        
        splitter.addWidget(sideBar)
        splitter.addWidget(workspace)

        # Set the initial size of each widget
        splitter.setSizes([200, 600])

        # Create a central widget and a layout for it
        centralWidget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(splitter)

        # Set the layout for the central widget
        centralWidget.setLayout(layout)

        # Set the central widget for the main window
        self.setCentralWidget(centralWidget)