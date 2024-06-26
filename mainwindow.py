from PySide6.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget, QFileDialog, QApplication, QLabel, QFrame, QHBoxLayout, QPlainTextEdit
from applicationlogic import ApplicationLogic
from applicationlogic import file_path
from PySide6.QtGui import QAction, QKeySequence, QShortcut, QFont, QFontDatabase, QPainter, QColor, QTextFormat
from newwindow import NewWindow
from PySide6.QtCore import Qt, QSize, QRect
from linenumber import LineNumberArea
from codeditor import CodeEditor
from syntaxhighlighter import PythonSyntaxHighlighter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#282c34;")

        self.textedit = CodeEditor()
        self.setCentralWidget(self.textedit)
        self.setWindowTitle("Notepad#")
        self.logic = ApplicationLogic(self)
        self.create_menu_bar()
        self.create_shortcuts()

        font = QFont("Source Code Pro for Powerline", 16)
        self.textedit.setFont(font)
        self.textedit.setStyleSheet("color: white;")
        self.highlighter = PythonSyntaxHighlighter(self.textedit.document())

    def create_menu_bar(self):
        menubar = self.menuBar()
        menubar.setStyleSheet("background-color:white;")

        # File menu
        file_menu = menubar.addMenu("File")

        # New action
        new_action = QAction("New", self)
        new_action.triggered.connect(self.logic.newfilestuff)
        file_menu.addAction(new_action)

        # Open action
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.logic.open_file)
        file_menu.addAction(open_action)

        # Save action
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.logic.save_file)
        file_menu.addAction(save_action)

        # Edit menu
        edit_menu = menubar.addMenu("Edit")

        # Copy action
        copy_action = QAction("Copy", self)
        copy_action.triggered.connect(self.logic.copy_file)
        edit_menu.addAction(copy_action)

        # paste action
        paste_action = QAction("Paste", self)
        paste_action.triggered.connect(self.logic.paste_text)
        edit_menu.addAction(paste_action)

        # Tools menu
        tools_menu = menubar.addMenu("Tools")

        # Open console action
        openconsole = QAction("Open Console", self)
        openconsole.triggered.connect(self.logic.open_console)
        tools_menu.addAction(openconsole)

        # Convert docx to html action
        parser = QAction("Parse Docx as HTML", self)
        parser.triggered.connect(self.logic.parser)
        tools_menu.addAction(parser)

        # Window menu
        window_menu = menubar.addMenu("Window")

        # New window action
        openwindow = QAction("New Window", self)
        openwindow.triggered.connect(self.open_window)
        window_menu.addAction(openwindow)

        # Settings
        settings = QAction("Settings", self)

    def open_window(self):
        newwindow = NewWindow()
        newwindow.show()

    def create_shortcuts(self):
        # Create shortcuts for actions
        shortcut_new = QShortcut(QKeySequence("Ctrl+N"), self)
        shortcut_new.activated.connect(self.logic.newfilestuff)

        shortcut_open = QShortcut(QKeySequence("Ctrl+O"), self)
        shortcut_open.activated.connect(self.logic.open_file)

        shortcut_save = QShortcut(QKeySequence("Ctrl+S"), self)
        shortcut_save.activated.connect(self.logic.save_file)

        shortcut_copy = QShortcut(QKeySequence("Ctrl+C"), self)
        shortcut_copy.activated.connect(self.logic.copy_file)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
