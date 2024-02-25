from PySide6.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout
from PySide6.QtCore import Qt, QMimeData, QPoint
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QMouseEvent
from gui.workspace.components.shape import Shape

class DropArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: lightblue; color: darkblue;")
        self.setAcceptDrops(True)
        
        startBlock = Shape("Start", self)
        startBlock.move(10, 10)
        startBlock.show()
        
        self.blocks = [startBlock]


    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):

        itemText = event.mimeData().text()
        newBlock = Shape(itemText, self)
        
        newBlock.move(event.position().toPoint() - QPoint(50,25))
        newBlock.show()
        self.blocks.append(newBlock)
        event.acceptProposedAction()

    def clearBlocks(self):
        for block in self.blocks:
            block.deleteLater()
        self.blocks.clear()
        
class Workspace(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: lightblue;")

        layout = QVBoxLayout()
        self.dropArea = DropArea()
        layout.addWidget(self.dropArea)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)