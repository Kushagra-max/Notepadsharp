from PySide6.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget, QFileDialog, QApplication
from applicationlogic import ApplicationLogic
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notepad#")
        self.textedit = QTextEdit()
        self.setCentralWidget(self.textedit)

        self.logic = ApplicationLogic(self)

        self.create_menu_bar()

    def create_menu_bar(self):
        menubar = self.menuBar()

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

        # Cut action
        copy_action = QAction("Copy", self)
        copy_action.triggered.connect(self.logic.copy_file)
        edit_menu.addAction(copy_action)
