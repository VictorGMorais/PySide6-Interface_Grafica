from pathlib import Path
import re

# Caminhos
RAIZ = Path(__file__).parent
FILES_DIR = RAIZ / 'files'
ICON_CALCULADORA = FILES_DIR / 'calculadora.png'


#sizing
BIG_SIZE = 40
MEDIUM_SIZE = 30
SMALL_SIZE = 20
WIDTH = 500
TXT_MARGIN = 8

# Tema Dark Elegante (ajustado ao seu estilo)
# CORES_BUTTONS_EXPECIAIS = """QPushButton {
#     background-color: #FF9800; /* Laranja vibrante (botão normal) */
#     border: 2px solid #444444 ; /* Cinza médio (borda) */
#     color: black; /* Preto (texto) */
#     padding: 10px 20px;
#     text-align: center;
#     font-size: 19px;
#     border-radius: 5px;
# }

# QPushButton:hover {
#     background-color: #E68900; /* Laranja mais escuro (hover) */
#     border: 2px solid #444444; /* Cinza médio (borda hover) */
#     color: black; /* Preto (texto hover) */
# }

# QPushButton:pressed {
#     background-color: #FFA726; /* Laranja mais claro (pressionado) */
#     color: black; /* Preto (texto pressionado) */
# }
# """

# CORES_BUTTONS_NUMERICOS = """QPushButton {
#     background-color: #364348; /* Cinza azulado escuro (botão normal) */
#     border: 2px solid #444444 ; /* Cinza médio (borda) */
#     color: white; /* Branco (texto) */
#     padding: 10px 20px;
#     font-size: 19px;
#     border-radius: 5px;
# }

# QPushButton:hover {
#     background-color: #252525; /* Cinza mais escuro (hover) */
#     color: white; /* Branco (texto hover) */
# }

# QPushButton:pressed {
#     background-color: #3A3A3A; /* Cinza intenso (pressionado) */
#     color: black; /* Preto (texto pressionado) */
# }
# """

# Tema Azul Frio & Neutro
CORES_BUTTONS_EXPECIAIS = f"""QPushButton {{
    background-color: #1565C0; /* Azul escuro intenso (botão normal) */
    border: 2px solid #1976D2; /* Azul médio (borda) */
    color: white; /* Branco (texto) */
    padding: 10px 20px;
    font-size: 17px;
    border-radius: 5px;
}}

QPushButton:hover {{
    background-color: #0D47A1; /* Azul mais escuro (hover) */
    border: 2px solid #1976D2; /* Azul médio (borda hover) */
    color: white; /* Branco (texto hover) */
}}

QPushButton:pressed {{
    background-color: #1E88E5; /* Azul vibrante (pressionado) */
    color: white; /* Branco (texto pressionado) */
}}
"""

CORES_BUTTONS_NUMERICOS = """QPushButton {
    background-color: #BBDEFB; /* Azul pastel claro (botão normal) */
    border: 2px solid #1976D2 ; /* Azul médio (borda) */
    color: black; /* Preto (texto) */
    padding: 10px 20px;
    font-size: 17px;
    border-radius: 5px;
}

QPushButton:hover {
    background-color: #90CAF9; /* Azul médio (hover) */
    color: black; /* Preto (texto hover) */
}

QPushButton:pressed {
    background-color: #64B5F6; /* Azul mais forte (pressionado) */
    color: black; /* Preto (texto pressionado) */
}
"""  



# def cor_geral():
#     MyWindow().setStyleSheet("background-color: #1E1E1E;")
#     Display().setStyleSheet(f'font-size: {SMALL_SIZE}px; background-color: #BBDEFB; color: black;')



# Tema Verde Vivo & Alegre
# CORES_BUTTONS_EXPECIAIS = """QPushButton {
#     background-color: #4CAF50; /* Verde intenso (botão normal) */
#     border: 2px solid #388E3C; /* Verde médio (borda) */
#     color: black; /* Branco (texto) */
#     padding: 10px 20px;
#     font-size: 19px;
#     border-radius: 5px;
# }

# QPushButton:hover {
#     background-color: #388E3C; /* Verde mais escuro (hover) */
#     border: 2px solid #388E3C; /* Verde médio (borda hover) */
#     color: black; /* Branco (texto hover) */
# }

# QPushButton:pressed {
#     background-color: #43A047; /* Verde vibrante (pressionado) */
#     color: black; /* Branco (texto pressionado) */
# }
# """

# CORES_BUTTONS_NUMERICOS = """QPushButton {
#     background-color: #C8E6C9; /* Verde pastel claro (botão normal) */
#     border: 2px solid #388E3C ; /* Verde médio (borda) */
#     color: black; /* Preto (texto) */
#     padding: 10px 20px;
#     font-size: 19px;
#     border-radius: 5px;
# }

# QPushButton:hover {
#     background-color: #A5D6A7; /* Verde médio (hover) */
#     color: black; /* Preto (texto hover) */
# }

# QPushButton:pressed {
#     background-color: #81C784; /* Verde mais forte (pressionado) */
#     color: black; /* Preto (texto pressionado) */
# }
# """

# Tema Vermelho Quente & Intenso
# CORES_BUTTONS_EXPECIAIS = """QPushButton {
#     background-color: #D32F2F; /* Vermelho intenso (botão normal) */
#     border: 2px solid #C62828; /* Vermelho médio (borda) */
#     color: white; /* Branco (texto) */
#     padding: 10px 20px;
#     font-size: 19px;
#     border-radius: 5px;
# }




#regex
NUM_OR_DOt_REGEX = re.compile(r'^[0-9.]$')

def isNumOrDot(txt: str) -> bool:
    return bool(NUM_OR_DOt_REGEX.search(txt))

def isEmpyt(txt: str) -> bool:
    return txt == ''

def isNumber(txt: str) -> bool:
    try:
        float(txt)
        return True
    except ValueError:
        return False
    