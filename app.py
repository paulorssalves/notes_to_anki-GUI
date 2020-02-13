from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from CSVwards import Ui_mainWindow
import sys
from model import Model

class MainWindowUIClass(Ui_mainWindow):
    def __init__(self):
        super().__init__()
        # adiciona as funcionalidades da classe Model a esta classe
        self.model = Model()

    def setupUi(self, MW):
        super().setupUi(MW)

    def refreshAll(self):
        """
        Atualiza o conteúdo da lousa que exibe o texto
        de acordo com o conteúdo do arquivo presentemente
        selecionado.
        """
        self.fullFileName.setText(self.model.getFileName())
        self.textEdit.setText(self.model.getFileContents())

    def returnPressedSlot(self):
        """
        Reage ao input dado à barra de texto onde se
        coloca o endereco/nome do arquivo. Retorna uma mensagem de
        erro se o arquivo for inválido.
        """
        fileName = self.fullFileName.text()
        if self.model.isValid(fileName):
            self.model.setFileName(self.fullFileName.text())
            self.refreshAll()
            
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Nome de arquivo inválido!\n" + fileName)
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok |
                                 QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.lineEdit.setText("")
            self.refreshAll()
            self.debugPrint("Arquivo inválido especificado: " + fileName)

    def convertSlot(self):
        """
        Converte o conteúdo da lousa que exibe o texto 
        em um arquivo csv
        """
        self.model.convert(self.textEdit.toPlainText())

    def browseSlot(self):
        """
        Abre uma janela de selecão de arquivos e define que
        arquivos .txt são o formato ideal.
        """
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Selecionar arquivo de texto para conversão",
            "",
            "Todos os arquivos (*);;Arquivos de texto(*.txt)",
            options=options)
        if fileName:
            self.model.setFileName(fileName)
            self.refreshAll()
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()
