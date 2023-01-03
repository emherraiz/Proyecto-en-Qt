from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('calculadora.ui')
        self.ui.show()
        self.ui.pushButton_0.clicked.connect(self.digito_0)
        self.ui.pushButton_1.clicked.connect(self.digito_1)
        self.ui.pushButton_2.clicked.connect(self.digito_2)
        self.ui.pushButton_3.clicked.connect(self.digito_3)
        self.ui.pushButton_4.clicked.connect(self.digito_4)
        self.ui.pushButton_5.clicked.connect(self.digito_5)
        self.ui.pushButton_6.clicked.connect(self.digito_6)
        self.ui.pushButton_7.clicked.connect(self.digito_7)
        self.ui.pushButton_8.clicked.connect(self.digito_8)
        self.ui.pushButton_9.clicked.connect(self.digito_9)
        self.ui.pushButton_punto.clicked.connect(self.digito_punto)
        self.ui.pushButton_suma.clicked.connect(self.suma)
        self.ui.pushButton_resta.clicked.connect(self.resta)
        self.ui.pushButton_multiplicacion.clicked.connect(self.multiplicacion)
        self.ui.pushButton_division.clicked.connect(self.division)
        self.ui.pushButton_igual.clicked.connect(self.igual)


    def digito_1(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '1')

    def digito_2(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '2')

    def digito_3(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '3')

    def digito_4(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '4')

    def digito_5(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '5')

    def digito_6(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '6')

    def digito_7(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '7')

    def digito_8(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '8')

    def digito_9(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '9')

    def digito_0(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '0')

    def digito_punto(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '.')

    def suma(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '+')

    def resta(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '-')

    def multiplicacion(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '*')

    def division(self):
        self.ui.Linea_de_resultados.setText(self.ui.Linea_de_resultados.text() + '/')

    def igual(self):
        try:
            self.ui.Linea_de_resultados.setText(str(eval(self.ui.Linea_de_resultados.text())))
        except:
            self.ui.Linea_de_resultados.setText('Error')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
