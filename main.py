#https://doc.qt.io/qtforpython-6/gettingstarted.html

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QMainWindow, QWidget


class MyWindow(QMainWindow):
    def __init__(self, parent = None ):
        super().__init__(parent)

        #definindo titulo da janela
        self.setWindowTitle('Calculadora')

        #definindo botoes
        self.botao1 = QPushButton('1')
        self.botao1.setStyleSheet('font-size: 19px; background-color: lightblue; border: 1px solid blue; padding: 5px;')
        self.botao1.clicked.connect(self.segunda_acao_marcada)
        self.botao2 = QPushButton('2')
        self.botao2.setStyleSheet('font-size: 19px; background-color: lightblue; border: 1px solid blue; padding: 5px;')
        self.botao3 = QPushButton('3')
        self.botao3.setStyleSheet('font-size: 19px; background-color: lightblue; border: 1px solid blue; padding: 5px;')
        self.botao4 = QPushButton('4')
        self.botao4.setStyleSheet('font-size: 19px; background-color: lightblue; border: 1px solid blue; padding: 5px;')
        self.botao5 = QPushButton('5')
        self.botao5.setStyleSheet('font-size: 19px; background-color: lightblue; border: 1px solid blue; padding: 5px;')
        self.botao6 = QPushButton('6')
        self.botao6.setStyleSheet('font-size: 19px; background-color: lightblue; border: 1px solid blue; padding: 5px;')
        self.botao7 = QPushButton('7')
        self.botao7.setStyleSheet('font-size: 19px; background-color: lightblue; border: 1px solid blue; padding: 5px;')
        self.botao8 = QPushButton('8')
        self.botao8.setStyleSheet('font-size: 19px; background-color: lightblue; border: 1px solid blue; padding: 5px;')
        self.botao9 = QPushButton('9')
        self.botao9.setStyleSheet('font-size: 19px; background-color: lightblue; border: 1px solid blue; padding: 5px;')
        self.botao0 = QPushButton('0')
        self.botao0.setStyleSheet('font-size: 19px; background-color: lightblue; border: 1px solid blue; padding: 5px;')

        #definindo janela simples
        self.central_widget = QWidget()

        #definindo layout
        self.g_layout = QGridLayout()
        self.central_widget.setLayout(self.g_layout)

        #aplicando layout
        self.g_layout.addWidget(self.botao1, 1, 1, 1, 1) #linha | coluna | linha espandida | coluna espandida
        self.g_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.g_layout.addWidget(self.botao3, 1, 3, 1, 1)

        #mostrando os botoes
        self.setCentralWidget(self.central_widget)

        #status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Teste de barra')

        #menu bar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('menu opçoes')
        self.primeira_acao = self.primeiro_menu.addAction('primeira açao')
        self.primeira_acao.triggered.connect(self.mensagem_status_bar)

        self.segunda_acao = self.primeiro_menu.addAction('segunda açao')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.segunda_acao_marcada)
        # self.segunda_acao.hovered.connect(self.segunda_acao_marcada)

    @Slot()
    def mensagem_status_bar(self):
            self.status_bar.showMessage('Meu slot foi executado')

    @Slot()
    def segunda_acao_marcada(self):
        print('esta marcado: ',self.segunda_acao.isChecked())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    app.exec()
