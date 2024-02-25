import sys
from PySide6.QtWidgets import QApplication, QSplitter, QWidget, QMainWindow, QTextEdit, QHBoxLayout
from PySide6.QtCore import Qt
from gui.app import App
from gui.settings import Settings

if not QApplication.instance():
    app = QApplication(sys.argv)
else:
    app = QApplication.instance()
settings = Settings()
window = App(settings)
window.show()
sys.exit(app.exec())