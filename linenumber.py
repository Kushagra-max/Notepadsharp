from PySide6.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget, QFileDialog, QApplication, QLabel, QFrame, QHBoxLayout, QPlainTextEdit
from applicationlogic import ApplicationLogic
from applicationlogic import file_path
from PySide6.QtGui import QAction, QKeySequence, QShortcut, QFont, QFontDatabase, QPainter, QColor, QTextFormat
from PySide6.QtCore import Qt, QSize, QRect

class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.editor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.editor.lineNumberAreaPaintEvent(event)
