
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QPushButton, QGridLayout

from variaveis_configs import SMALL_SIZE, isNumOrDot, isEmpyt, CORES_BUTTONS_EXPECIAIS , CORES_BUTTONS_NUMERICOS

#classe da janela principal
class MyWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setStyleSheet("background-color: #1E1E1E;")

        #adicionar nome a janela
        self.setWindowTitle('Calculadora')

        #criar janela principal
        self.central_window = QWidget()

        #criar layout
        self.vertical_layout = QVBoxLayout()
        self.central_window.setLayout(self.vertical_layout)

        #liga a janela ao main window
        self.setCentralWidget(self.central_window)    

    def addWidgetLayout(self, widget : QWidget):
        self.vertical_layout.addWidget(widget)

    def adjustFixedSize(self):
        #ultima coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        
class Button(QPushButton):
    def __init__(self, txt: str, parent : QWidget | None = None) -> None:
        super().__init__(txt, parent)
        self.styleButton()

    def styleButton(self):
        self.setStyleSheet('font-size: 20px;')
        font = self.font()
        font.setPixelSize(SMALL_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class GridButtons(QGridLayout):
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._gridLayout = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '=']]
        
        self._make_grid()

    def _make_grid(self):
        for i,linha in enumerate(self._gridLayout):
            for j,coluna in enumerate(linha):
                button = Button(coluna)

                if not isNumOrDot(coluna) and not isEmpyt(coluna):
                    self.addWidget(button, i, j)
                    button.setStyleSheet(CORES_BUTTONS_EXPECIAIS)
                else:
                    self.addWidget(button, i, j)
                    button.setStyleSheet(CORES_BUTTONS_NUMERICOS)