import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from main_window import MyWindow, GridButtons
from display import Display , Info
from variaveis_configs import ICON_CALCULADORA



if __name__ == '__main__':
    #criar aplicação
    app = QApplication(sys.argv)
    window = MyWindow()

    #adicionar icone a janela
    icon = QIcon(str(ICON_CALCULADORA))
    window.setWindowIcon(icon)

    #chamar info
    info = Info('0')
    window.addWidgetLayout(info)

    #chamar display
    display = Display()
    window.addWidgetLayout(display)

    #grid de botões
    grid = GridButtons(display, info)
    window.vertical_layout.addLayout(grid)

    
    # ajustar tamanho da janela
    window.adjustFixedSize()

    #mostrar janela
    window.show()
    app.exec()