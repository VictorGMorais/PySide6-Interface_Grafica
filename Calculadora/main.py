import sys
from main_window import MyWindow
from PySide6.QtWidgets import QApplication, QLabel


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MyWindow()

    label = QLabel('HELLO WORLD')
    window.layout.addWidget(label)

    window.adjustFixedSize()
    window.show()
    app.exec()