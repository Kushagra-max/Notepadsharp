from PySide6.QtGui import QAction, QClipboard
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
import sys
import subprocess


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
        file_dialog = QFileDialog(self.main_window)
        file_path, _ = file_dialog.getOpenFileName(self.main_window, "Open File", "", "Text files (*.txt);;All files (*)")
        if file_path:
            with open(file_path, "r") as file:
                self.main_window.textedit.setPlainText(file.read())

    def save_file(self):
        file_dialog = QFileDialog(self.main_window)
        file_path, _ = file_dialog.getSaveFileName(self.main_window, "Save File", "", "Text files (*.txt);;All files (*)")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.main_window.textedit.toPlainText())
    def copy_file(self):
        text_to_copy = self.main_window.textedit.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text_to_copy)

    def open_console(self):
    # Check if the system is Windows
        if sys.platform.startswith('win'):
            subprocess.Popen('cmd', shell=True)
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
