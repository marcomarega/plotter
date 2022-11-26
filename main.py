import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface import Ui_MainWindow
from math import *

from PyQt5 import QtCore, QtWidgets

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Plotter(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Plotter, self).__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.lineEdit.textEdited.connect(self.run)

    def run(self):
        self.graphicsView.clear()
        function = self.lineEdit.text()
        xs = [x / 100 for x in range(-1000, 1001)]
        ys = list()
        for x in xs:
            try:
                y = eval(function)
                ys.append(y)
            except Exception:
                xs.remove(x)
        self.graphicsView.plot(xs, ys)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wid = Plotter()
    wid.show()
    sys.exit(app.exec())
