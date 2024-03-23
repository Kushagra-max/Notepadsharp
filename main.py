import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QMenuBar, QFileDialog, QMessageBox
from PySide6.QtGui import QAction


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Notepad#")
        self.textedit = QTextEdit()
        self.setGeometry(100, 60, 1000, 800)

        # Set the central widget
        central_widget = QWidget()
        self.setCentralWidget(self.textedit)


        # Create a layout and add the QTextEdit widget to it
        layout = QVBoxLayout(self.textedit)
        QApplication.setAttribute(Qt.AA_DontUseNativeMenuBar)

        self.menubar()


    def menubar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        # File
        new_action = QAction("New", self)
        file_menu.addAction(new_action)
        new_action.triggered.connect(self.alerthandler)


        open_action = QAction("Open", self)
        file_menu.addAction(open_action)
        open_action.triggered.connect(self.open_file)

        save_action = QAction("Save", self)
        file_menu.addAction(save_action)
        save_action.triggered.connect(self.save_file)

    # open
    def open_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Open File", "", "Text files (*.txt);;All files (*)")
        if file_path:
            with open(file_path, "r") as file:
                self.textedit.setPlainText(file.read())
    # save
    def save_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getSaveFileName(self, "Save File", "", "Text files (*.txt);;All files (*)")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.textedit.toPlainText())
    # new
    def new_file(self):
        self.textedit.clear()

    # alerhandler
    def alerthandler(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Unsaved data wil be deleted.")
        msgBox.setWindowTitle("Unsaved data wil be deleted.")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.new_file()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()