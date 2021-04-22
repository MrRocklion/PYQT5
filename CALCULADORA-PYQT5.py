import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout ,QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("TEST DE PYTHON BY DAVID")
window.setFixedWidth(400)
window.move(500,500)
window.setStyleSheet("background: #C70039;")
grid = QGridLayout()
#variables globales
def create_button(answer):
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(350)
    button.setStyleSheet(
                        "*{border: 4px solid '##000000';"+
                        "color: white;"+
                        "font-family: 'shanti';"+
                        "font-size: 16px;"+
                        "border-radius: 25px;"+
                        "padding: 15px 0;"+
                        "margin-top: 20px}"+
                        "*:hover{background: '#1D3464'}"
            )
    return button
def frame1():
    label1 = QLabel("CALCULADORA")
    label1.setStyleSheet("color: white;"+"font-size: 70px;")
    label1.setAlignment(QtCore.Qt.AlignCenter)
    label1.setFont(QtGui.QFont("Bellyn Natural"))
    label2 = QLabel("BASICA")
    label2.setStyleSheet("color: white;"+"font-size: 70px;")
    label2.setAlignment(QtCore.Qt.AlignCenter)
    label2.setFont(QtGui.QFont("Bellyn Natural"))
    label3 = QLabel("Nro-1")
    label3.setStyleSheet("color: white;"+"font-size: 25px;"+"padding: 5px 0")
    label3.setAlignment(QtCore.Qt.AlignLeft)
    label3.setFont(QtGui.QFont("Bellyn Natural"))
    label4 = QLabel("Nro2")
    label4.setStyleSheet("color: white;"+"font-size: 25px;"+"padding: 5px 0")
    label4.setAlignment(QtCore.Qt.AlignLeft)
    label4.setFont(QtGui.QFont("Bellyn Natural"))
    label5 = QLabel("Resultado")
    label5.setStyleSheet("color: white;"+"font-size: 25px;"+"padding: 5px 0")
    label5.setAlignment(QtCore.Qt.AlignLeft)
    label5.setFont(QtGui.QFont("Bellyn Natural"))
    resultado = QLabel()
    resultado.setStyleSheet("color: white;"+"font-size: 25px;"+"padding: 5px 0")
    resultado.setAlignment(QtCore.Qt.AlignCenter)
    resultado.setFont(QtGui.QFont("Source Sans Pro"))
    #entradas de texto
    text1 = QLineEdit()
    text1.setStyleSheet("*{border: 4px solid  '#000000';"+"border-radius: 25px;"+"font-size: 25px;"+"color: 'white';"+"padding: 5px 0;}")
    text1.setAlignment(QtCore.Qt.AlignCenter)
    text2 = QLineEdit()
    text2.setStyleSheet("*{border: 4px solid  '#000000';"+"border-radius: 25px;"+"font-size: 25px;"+"color: 'white';"+"padding: 5px 0;}")
    text2.setAlignment(QtCore.Qt.AlignCenter)
    #logotipo david
    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 5px;")
    #funciones matetamticas
    def suma():
        a = int(text1.text())
        b = int(text2.text())
        resultado.setText(str(a+b))
    def resta():
        a = int(text1.text())
        b = int(text2.text())
        resultado.setText(str(a-b))
    def division():
        a = int(text1.text())
        b = int(text2.text())
        resultado.setText(str(a/b))
    def multiplicacion():
        a = int(text1.text())
        b = int(text2.text())
        resultado.setText(str(a*b))
    #botones
    sumar = create_button("sumar")
    restar = create_button("restar")
    multiplicar = create_button("multiplicar")
    dividir = create_button("dividir")
    sumar.clicked.connect(suma)
    restar.clicked.connect(resta)
    multiplicar.clicked.connect(multiplicacion)
    dividir.clicked.connect(division)
    #ubicacion en grid
    grid.addWidget(label1, 0, 0,1,2)
    grid.addWidget(label2, 1, 0,1,2)
    grid.addWidget(label3, 2, 0)
    grid.addWidget(text1, 2, 1)
    grid.addWidget(label4, 3, 0)
    grid.addWidget(text2, 3, 1)
    grid.addWidget(label5, 4, 0)
    grid.addWidget(resultado, 4, 1)
    grid.addWidget(sumar, 5, 0,1,2)
    grid.addWidget(restar, 6, 0,1,2)
    grid.addWidget(multiplicar, 7, 0,1,2)
    grid.addWidget(dividir, 8, 0,1,2)
    grid.addWidget(logo, 9, 0,1,2)


frame1()
#ejecucion del programa
window.setLayout(grid)
window.show()
sys.exit(app.exec())