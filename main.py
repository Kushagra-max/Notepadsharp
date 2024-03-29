import sys
from PySide6.QtWidgets import QApplication

from mainwindow import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.resize(640, 360)
window.show()
sys.exit(app.exec())