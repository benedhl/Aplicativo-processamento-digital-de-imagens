import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon

fonteLegenda = QFont("Times", 10)
fonteValor = QFont("Times", 18)


class JanelaValorLimitePretoBranco(QWidget):

    def __init__(self):
        super(JanelaValorLimitePretoBranco, self).__init__()
        self.setWindowTitle("Conversão para Preto e Branco")
        self.setWindowIcon(QIcon("icones/icon.jpg"))
        self.setGeometry(700, 350, 250, 150)
        self.setFixedSize(250, 150)
        self.setWindowModality(Qt.ApplicationModal)
        self.valorSlider = 0
        self.initUI()
        self.show()

    '''Chamar métodos que criam a interface'''

    def initUI(self):
        self.criarWidgets()
        self.gerarLayouts()

    '''Cria os widgets que encorporam o Menu e widgets que executaram ações'''

    def criarWidgets(self):
        self.legenda = QLabel("Defina um valor limite para conversão")
        self.legenda.setAlignment(Qt.AlignCenter)
        self.legenda.setFont(fonteLegenda)
        self.textoValor = QLabel("0")
        self.textoValor.setAlignment(Qt.AlignCenter)
        self.textoValor.setFont(fonteValor)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.exibirValor)

        self.enviarValor = QPushButton('Enviar Valor')
        self.enviarValor.setToolTip("Enviar valor escolhido")

    def gerarLayouts(self):
        vbox = QVBoxLayout()

        vbox.addWidget(self.legenda)
        vbox.addStretch()
        vbox.addWidget(self.textoValor)
        vbox.addStretch()
        vbox.addWidget(self.slider)
        vbox.addWidget(self.enviarValor)
        self.setLayout(vbox)

    def exibirValor(self):
        self.valorSlider = self.slider.value()
        self.textoValor.setText(str(self.valorSlider))

def main():
    app = QApplication(sys.argv)
    win = JanelaValorLimitePretoBranco()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
