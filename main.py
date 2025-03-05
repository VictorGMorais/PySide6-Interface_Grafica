#https://doc.qt.io/qtforpython-6/gettingstarted.html

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QMainWindow, QWidget


app = QApplication(sys.argv)

botao1 = QPushButton('Click')
botao1.setStyleSheet('font-size: 19px')

botao2 = QPushButton('Checkout')
botao2.setStyleSheet('font-size: 19px')

botao3 = QPushButton('click')
botao3.setStyleSheet('font-size: 19px')

central_widget = QWidget()
layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1) #linha | coluna | linha espandida | coluna espandida
layout.addWidget(botao3, 1, 2, 1, 1)

layout.addWidget(botao2, 2, 1, 1, 2)

central_widget.show()
app.exec()
