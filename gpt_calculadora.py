# import sys
# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Calculadora')


#         self.result = []
#         self.botao1 = self.make_botao('1')
#         self.botao2 = self.make_botao('2')
#         self.botao3 = self.make_botao('3')
#         self.botao4 = self.make_botao('4')
#         self.botao5 = self.make_botao('5')
#         self.botao6 = self.make_botao('6')
#         self.botao7 = self.make_botao('7')
#         self.botao8 = self.make_botao('8')
#         self.botao9 = self.make_botao('9')
#         self.botao_adc = self.make_botao('+')
#         self.botao_dcm = self.make_botao('-')
#         self.botao0 = self.make_botao('0')

#         for bt in [self.botao1, self.botao2, self.botao3, self.botao4, self.botao5, 
#                    self.botao6, self.botao7, self.botao8, self.botao9, self.botao_adc, 
#                    self.botao_dcm, self.botao0]:
#             bt.clicked.connect(lambda _, b=bt.text(): self.operacao(b))
        
#         layout = QGridLayout()
#         layout.addWidget(self.botao1,1, 1)
#         layout.addWidget(self.botao2,1, 2)
#         layout.addWidget(self.botao3,1, 3)
#         layout.addWidget(self.botao4,2, 1)
#         layout.addWidget(self.botao5,2, 2)
#         layout.addWidget(self.botao6,2, 3)
#         layout.addWidget(self.botao7,3, 1)
#         layout.addWidget(self.botao8,3, 2)
#         layout.addWidget(self.botao9,3, 3)
#         layout.addWidget(self.botao_adc,4, 1)
#         layout.addWidget(self.botao0,4, 2)
#         layout.addWidget(self.botao_dcm,4, 3)

#         self.setLayout(layout)


#     def make_botao(self,txt):
#         self.btn = QPushButton(txt)
#         self.btn.setStyleSheet('font-size: 14; background-color: lightblue; border: 1px solid blue; padding: 5px;')
#         return self.btn

#     def operacao(self, valor):
#         self.result.append(valor)
#         print(self.result)
               
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec()

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculadora')
        self.result = []  # Armazena os valores digitados

        # Exibição do resultado
        self.display = QLabel('')
        self.display.setStyleSheet('font-size: 24px; border: 1px solid black; padding: 5px;')

        # Criando os botões
        botoes = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '+', '0', '-'
        ]

        layout = QGridLayout()
        self.botoes_objs = {}  # Dicionário para armazenar os botões criados

        for i, texto in enumerate(botoes):
            bt = QPushButton(texto)
            bt.setStyleSheet('font-size: 18px; background-color: lightblue; padding: 10px;')
            bt.clicked.connect(self.capturar_botao)  # Conectando sem lambda!
            self.botoes_objs[texto] = bt  # Armazena no dicionário
            layout.addWidget(bt, i // 3, i % 3)  # Organiza na grade

        # Layout principal
        vbox = QVBoxLayout()
        vbox.addWidget(self.display)
        vbox.addLayout(layout)
        self.setLayout(vbox)

    def capturar_botao(self):
        """Captura o botão clicado e atualiza o display."""
        botao = self.sender()  # Pega o botão que disparou o evento
        if botao:
            valor = botao.text()
            self.result.append(valor)  # Armazena na lista
            self.display.setText(''.join(self.result))  # Atualiza o display

app = QApplication(sys.argv)
window = Calculadora()
window.show()
app.exec()
