from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QSplitter
from PySide6.QtCore import Qt, QMimeData, QPoint
from PySide6.QtGui import QDrag, QPixmap, QPainter, QPen
from gui.workspace.workspace import DropArea

class DraggableListWidget(QListWidget):
    def __init__(self, settings, parent=None):
        super().__init__(parent)
        self.settings = settings
        self.setDragEnabled(True)
        self.setStyleSheet("QListWidget { background-color: lightblue; color: darkblue; }")
    
    def startDrag(self, supportedActions):
        item = self.currentItem()

        mimeData = QMimeData()
        mimeData.setText(item.text())

        drag = QDrag(self)
        drag.setMimeData(mimeData)

        pixmap = self.createShapePixmap(self.getItemShape(item.text()))
        drag.setPixmap(pixmap)
        hotSpot = QPoint(50, 25)
        drag.setHotSpot(hotSpot)
        # Start the drag operation
        drag.exec_(Qt.MoveAction)

    def getItemShape(self, text):
        if text.startswith("Rectangle"):
            return "Rectangle"
        elif text.startswith("Oval"):
            return "Oval"
        elif text.startswith("Circle"):
            return "Circle"
        else:
            return "Default"

    def createShapePixmap(self, shape):
        # Create a pixmap with the desired shape
        pixmap = QPixmap(200, 200)  # Adjust the size as needed
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        
        painter.setRenderHints(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 2))
        # Draw different shapes based on the specified shape
        if shape == "Rectangle":
            painter.drawRect(2, 2, 100, 50)
        elif shape == "Oval":
            painter.drawEllipse(2, 2, 100, 50)
        elif shape == "Circle":
            painter.drawEllipse(2, 2, 100, 50)
        else:
            painter.drawRect(2, 2, 100, 50)
        painter.end()
        return pixmap
        
class SideBar(QWidget):
    def __init__(self, settings, parent=None):
        super().__init__(parent)
        self.initUI(settings)

    def initUI(self, settings):
        # Create the splitter
        splitter = QSplitter(Qt.Vertical, self)
        
        # Create and add draggable list widgets to the splitter
        actionsWidget = DraggableListWidget(settings)
        actionsWidget.addItem("Rectangle")
        actionsWidget.addItem("Oval")
        actionsWidget.addItem("Circle")
        
        flowsWidget = DraggableListWidget(settings)
        flowsWidget.addItem("Rectangle 2")
        flowsWidget.addItem("Oval 2")
        flowsWidget.addItem("Circle 2")
        
        splitter.addWidget(actionsWidget)
        splitter.addWidget(flowsWidget)
        
        # Create a layout for the sidebar and add the splitter to it
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(splitter)