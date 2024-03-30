from PySide6.QtGui import QAction, QClipboard
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog
import sys
import subprocess
file_path = "none"

class ApplicationLogic:
    def __init__(self, main_window):
        self.main_window = main_window

    def newfilestuff(self):
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information)
        msg.setText("Unsaved data will be deleted") 
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msg.exec()
        if returnValue == QMessageBox.Ok:
            self.new_file()



    def new_file(self): 
        self.main_window.textedit.clear()

    def open_file(self):
        global file_path
        file_type = "Text files (*.txt);;Python Files (*.py);;C Files (*.c);;HTML Files (*.html);;All files (*)"
        file_dialog = QFileDialog(self.main_window)
        file_path, _ = file_dialog.getOpenFileName(self.main_window, "Open File", "", file_type)
        if file_path:
            with open(file_path, "r") as file:
                self.main_window.textedit.setPlainText(file.read())
                self.main_window.setWindowTitle(f"Notepad# - {file_path}")



    def save_file(self):
        file_type = "Text files (*.txt);;Python Files (*.py);;C Files (*.c);;HTML Files (*.html);;All files (*)"
        file_dialog = QFileDialog(self.main_window)
        file_path, _ = file_dialog.getSaveFileName(self.main_window, "Save File", "", file_type)
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.main_window.textedit.toPlainText())
                self.main_window.setWindowTitle(f"Notepad# - {file_path}")

    def copy_file(self):
        text_to_copy = self.main_window.textedit.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text_to_copy)

    def open_console(self):
    # Check if the system is Windows
        if sys.platform.startswith('win'):
            subprocess.Popen(['cmd', '/K'], shell=True)
    # Check if the system is Linux or macOS
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            subprocess.Popen(['open', '-a', 'Terminal'], shell=False)

        else:
            print("Unsupported platform")

    # Paste Text
    def paste_text(self):
        clipboard = QApplication.clipboard()
        text_to_paste = clipboard.text()
        self.main_window.textedit.insertPlainText(text_to_paste)
