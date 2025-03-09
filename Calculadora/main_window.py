from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QPushButton, QGridLayout
from typing import TYPE_CHECKING

from variaveis_configs import SMALL_SIZE, isNumOrDot, isEmpyt, isNumber, CORES_BUTTONS_EXPECIAIS , CORES_BUTTONS_NUMERICOS


if TYPE_CHECKING:
    from display import Display, Info

#classe da janela principal
class MyWindow(QMainWindow):
    def __init__(self , parent: QWidget | None = None, *args, **kwargs) -> None:
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

        self.setMaximumSize(400, 600)


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
        self.setMinimumSize(85, 75)
        self.setMaximumSize(85, 75)
        # self.setCheckable(True)  #marca/desmarca

class GridButtons(QGridLayout):
    
    def __init__(self ,display: 'Display', info: 'Info',  parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._gridLayout = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', 'x'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '=']]
        
        self.display = display
        self.info = info
        self._equation = ''
        self._equationInit = '0'
        self.equation = self._equationInit
        self._left = None
        self._right = None
        self._operator = None


        self._make_grid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(self._equation)


    def _make_grid(self):
        for i,linha in enumerate(self._gridLayout):
            for j,coluna in enumerate(linha):
                button = Button(coluna)
                
                

                if not isNumOrDot(coluna) and not isEmpyt(coluna):
                    button.setStyleSheet(CORES_BUTTONS_EXPECIAIS)
                    self._config_special_button(button)
                else:
                    button.setStyleSheet(CORES_BUTTONS_NUMERICOS)

                

                self.addWidget(button, i, j)
                slot = self._make_slot(self._print_button_display, button)
                self._ConnectClicked(button, slot)

    def _ConnectClicked(self, button, slot):
        return button.clicked.connect(slot)
    
    def _config_special_button(self, button):
        text = button.text()

        if text == 'C':
            self._ConnectClicked(button,self._clear_display)

        elif text in '-+x/^':
            self._ConnectClicked(button, self._make_slot(self._operator_click, button))

        elif text == '=':
            self._ConnectClicked(button, self._calculate)
    
    def _make_slot(self, func, *args, **kwargs):
        @Slot(bool)
        def real_slot(_):
            func(*args, **kwargs)
        return real_slot

    def _print_button_display(self,button):
        button_text = button.text()
        verifica_entrada_num = self.display.text() + button_text

        if not isNumber(verifica_entrada_num):
            return
        self.display.insert(button_text)
    
    def format_number(self, num: float) -> str:
        num = float(num)  # Garante que é um float
    
        if abs(num) >= 1e10 or (0 < abs(num) < 1e-6):  # Se for muito grande ou pequeno
            return f"{num:.6e}"  # Exibe em notação científica com 6 casas

        return str(int(num)) if num.is_integer() else str(num)


    def _clear_display(self):
        self.equation = self._equationInit
        self._left = None
        self._right = None
        self._operator = None
        self.display.clear()

    def _operator_click(self, button):
        button_text = button.text()
        display_text = self.display.text()
        self.display.clear()

        if not isNumber(display_text) and self._left is None:
            return
        
        if self._left is None:
            self._left = float(display_text)
           
        self._operator = button_text
        self.equation = f'{self.format_number(self._left)} {self._operator}'

    def _calculate(self):
        display_text = self.display.text()
        if not isNumber(display_text) or self._operator is None:
            return
        
        self._right = float(display_text)
        self.display.clear()

        if self._operator == '+':
            result = self._left + self._right
        elif self._operator == '-':
            result = self._left - self._right
        elif self._operator == 'x':
            result = self._left * self._right
        elif self._operator == '^':
            result = self._left ** self._right
        elif self._operator == '/':
            if self._right == 0:
                self._clear_display()
                self.equation = 'Erro: Divisão por zero'

                return
            result = self._left / self._right
        else:
            return
        
        self.equation = f'{self.format_number(self._left)} {self._operator} {self.format_number(self._right)} = {self.format_number(result)}'
        self._left = result
        self._right = None
        self._operator = None
        self.display.setText(self.format_number(result))
