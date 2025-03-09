from PySide6.QtWidgets import QLineEdit, QLabel , QWidget
from PySide6.QtCore import Qt


from variaveis_configs import SMALL_SIZE, TXT_MARGIN, WIDTH

class Display(QLineEdit):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        margins = [TXT_MARGIN for _ in range(4)]  #tamanho das margens
        
        #definindo estilo do display
        self.setStyleSheet(f'font-size: {SMALL_SIZE}px; background-color: #BBDEFB; color: black;') 
       
        
        self.setMaximumHeight(SMALL_SIZE * 2.2)  #definindo tamanho do display
        
        self.setMaximumWidth(WIDTH)  #definindo largura do display
       
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  #definindo alinhamento do texto a direita
        
        self.setTextMargins(*margins)  #definindo margens

        # self.setPlaceholderText('0') #definindo texto placeholder
   

class Info(QLabel):
    def __init__(self, txt: str, parent : QWidget | None = None) -> None:
        super().__init__(txt, parent)
        self.setStyleSheet(f'font-size: {SMALL_SIZE}px; color: #778899;')  #definindo estilo do display / texto cinza ardozia claro
        
        # self.setStyleSheet(f'font-size: {SMALL_SIZE}px;')  #definindo tamanho da fonte
        
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  #definindo alinhamento do texto a direita
        
        # self.setText('0') #definindo texto placeholder






