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

CORES_BUTTONS_EXPECIAIS = """QPushButton {
    background-color: #FFA500; /* Laranja claro */
    border: 2px solid #AA3c08; /* Laranja forte (borda) */
    color: #0F2B39; /* Forte (texto) */
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    border-radius: 5px;
}

QPushButton:hover {
    background-color: #FF8C00; /* Laranja médio (hover) */
    border: 2px solid #FF6347; /* Laranja escuro (borda hover) */
}

QPushButton:pressed {
    background-color: #FF6347; /* Laranja escuro (pressionado) */
}
"""

CORES_BUTTONS_NUMERICOS = """QPushButton {
    background-color: #1fbdb5; /* Claro */
    border: 2px solid #1F5673; /* Médio (borda) */
    color: #0F2B39; /* Forte (texto) */
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    border-radius: 5px;
}

QPushButton:hover {
    background-color: #1F5673; /* Médio (hover) */
    color: #C8DCE6; /* Claro (texto hover) */
}

QPushButton:pressed {
    background-color: #0000FF; /* Forte (pressionado) */
    color: #C8DCE6; /* Claro (texto pressionado) */
}"""
    

#regex
NUM_OR_DOt_REGEX = re.compile(r'^[0-9.]$')

def isNumOrDot(txt: str) -> bool:
    return bool(NUM_OR_DOt_REGEX.search(txt))

def isEmpyt(txt: str) -> bool:
    return txt == ''