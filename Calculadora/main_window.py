import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        #adicionar nome a janela
        self.setWindowTitle('Calculadora')

        #criar janela principal
        self.central_window = QWidget()

        #criar layout
        self.layout = QVBoxLayout()
        self.central_window.setLayout(self.layout)

        #liga a janela ao main window
        self.setCentralWidget(self.central_window)


    def adjustFixedSize(self):
        #ultima coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        
    