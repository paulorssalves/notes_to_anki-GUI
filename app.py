from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from CSVwards import Ui_mainWindow
import sys

class MainWindowUIClass(Ui_mainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MW):
        super().setupUi(MW)

    def returnPressedSlot(self):
        print("return key pressed in lineEdit widget")

    def convertSlot(self):
        print("convert button pressed")

    def browseSlot(self):
        print("browseSlot pressed")
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()
