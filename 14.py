from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("pretty calc")
    window.setGeometry(300, 250, 350, 200)
    window.show()
    sys.exit(app.exec_())

