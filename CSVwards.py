# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CSVwards.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QObject
import webbrowser


class Ui_mainWindow(QObject):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(345, 534)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fullFileName = QtWidgets.QLineEdit(self.centralwidget)
        self.fullFileName.setObjectName("fullFileName")
        self.horizontalLayout.addWidget(self.fullFileName)
        self.selectFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectFileButton.setObjectName("selectFileButton")
        self.horizontalLayout.addWidget(self.selectFileButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setObjectName("convertButton")
        self.verticalLayout_2.addWidget(self.convertButton)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 345, 25))
        self.menubar.setObjectName("menubar")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        mainWindow.setMenuBar(self.menubar)
        self.openTutorialPage = QtWidgets.QAction(mainWindow)
        self.openTutorialPage.setWhatsThis("")
        self.openTutorialPage.setObjectName("openTutorialPage")
        self.openTutorialPage.triggered.connect(self.OpenTutorial)

        self.infoButton = QtWidgets.QAction(mainWindow)
        self.infoButton.setObjectName("infoButton")
        self.menuAjuda.addAction(self.infoButton)
        self.menuAjuda.addAction(self.openTutorialPage)
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(mainWindow)
        self.selectFileButton.clicked.connect(self.browseSlot)
        self.convertButton.clicked.connect(self.convertSlot)
        self.fullFileName.returnPressed.connect(self.returnPressedSlot)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Notes To Anki"))
        self.selectFileButton.setText(_translate("mainWindow", "Abrir"))
        self.convertButton.setText(_translate("mainWindow", "Converter"))
        self.menuAjuda.setTitle(_translate("mainWindow", "Ajuda"))
        self.openTutorialPage.setText(_translate("mainWindow", "Tutorial"))
        self.openTutorialPage.setToolTip(_translate("mainWindow", "Abre a página de tutorial no GitHub"))
        self.openTutorialPage.setStatusTip(_translate("mainWindow", "Abre a página de tutorial no GitHub"))
        self.infoButton.setText(_translate("mainWindow", "Info"))
        self.infoButton.setStatusTip(_translate("mainWindow", "Explica o propósito do programa"))

    @pyqtSlot()
    def OpenTutorial(self):
         webbrowser.open('https://github.com/tr4zodone/notes_to_anki-GUI')
    
    @pyqtSlot()
    def returnPressedSlot(self):
        pass

    @pyqtSlot()
    def convertSlot(self):
        pass

    @pyqtSlot()
    def browseSlot(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
