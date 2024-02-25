from PySide6.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout
from PySide6.QtCore import Qt, QMimeData, QPoint
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QMouseEvent

class Shape(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(100, 50)
        self.setStyleSheet("background-color: lightgrey; border: 1px solid black;")
        self.setAutoFillBackground(True)
        self.setMouseTracking(True)
        self.moving = False
        self.offset = QPoint()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.moving = True
            self.offset = event.position().toPoint()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.moving:
            self.move(self.pos() + event.position().toPoint() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.moving = False