import os
import shutil
from win32api import GetSystemMetrics
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from PyQt5.QtGui import QPixmap


def ocultarDiretorioImgResultado():
    os.system("attrib +h " + 'imagensResultado')


class ManipulacaoImagens(QWidget):
    def __init__(self, imagemOriginal, controleVisibilidadeItens, controleChecagemFiltros):
        super(ManipulacaoImagens, self).__init__()
        self.imagemOriginal = imagemOriginal
        self.imagemResultado = 'imagensResultado/imagemTransformada'
        self.extensaoImagemResultado = '.ppm'
        self.extensaoImagemOriginal = ''
        self.endImagemOriginal = ''
        self.endImagemResultado = ''
        self.controleVisibilidadeItens = controleVisibilidadeItens
        self.controleChecagemFiltros = controleChecagemFiltros

    '''Abre imagem selecionada pelo usuário e mantêm oculta diretório que mantem cópias de imagens anteriores que foram 
    transformadas, também solicita habilitar visibilidade dos menus e ações, remoção de cópias de imagens anteriores 
    transformadas, zera porcentagem da barra de progresso, defini pixmap da Imagem a ser exibida'''

    def abrirImagem(self):
        ocultarDiretorioImgResultado()

        arquivoImagem, _ = QFileDialog.getOpenFileName(self, caption="Abrir Imagem",
                                                       directory=QtCore.QDir.currentPath(),
                                                       filter='Imagens(*.ppm; *.pgm; *.pbm)',
                                                       initialFilter='Imagens(*.ppm; *.pgm; *.pbm)')

        if arquivoImagem:
            self.excluirCopiaImgTransformada()
            self.controleChecagemFiltros.removerChecagemFiltrosUsados()
            self.endImagemOriginal = arquivoImagem
            self.pixmapImagem = QPixmap(self.endImagemOriginal)
            self.extensaoImagemOriginal = os.path.splitext(os.path.basename(arquivoImagem))[1]
            self.extrairInfoImagem()
            self.exibirImagem()
            self.controleVisibilidadeItens.alterarVisibilidadeItensMenuTransformacoes(self.extensaoImagemOriginal)

    '''Exibe informações sobre aplicativo e imagem quando selecionado menu Sobre'''

    def extrairInfoImagem(self):
        try:
            self.parts = self.endImagemOriginal.rpartition('/')
            self.nomeimagem = self.parts[2]
            self.leituraimagem = open(self.endImagemOriginal, "r+")
            self.tipoimagem = self.leituraimagem.readline()
            self.comentarioimagem = self.leituraimagem.readline()
            self.dimensoesimagem = self.leituraimagem.readline()
            self.dimensoesimagem = self.dimensoesimagem.split()
            self.larguraimagem = self.dimensoesimagem[0]
            self.alturaimagem = self.dimensoesimagem[1]
        except:
            pass

    def exibirImagem(self):
        if self.pixmapImagem.width() > int(GetSystemMetrics(0) / 2) or \
                self.pixmapImagem.height() > int(GetSystemMetrics(1) / 2):
            self.pixmapImagem = self.pixmapImagem.scaled(int(GetSystemMetrics(0) / 2), int(GetSystemMetrics(1) / 2),
                                                         QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

        self.imagemOriginal.setPixmap(self.pixmapImagem)
        self.imagemOriginal.setAlignment(QtCore.Qt.AlignCenter)

    '''Salva Imagem com nome de arquivo e diretório escolhidos pelo usuário. Procura pela imagem transformada, caso
    não exista, é salvo a imagem original com o nome que o usuário escolher'''

    def salvarImagemComo(self):
        try:
            if self.endImagemOriginal != '':
                imagemSalvaComo, tipos = QFileDialog.getSaveFileName(self, caption='Salvar como',
                                                                     directory=QtCore.QDir.currentPath(),
                                                                     filter='Imagens(*.ppm; *.pgm; *.pbm)',
                                                                     initialFilter='Imagens(*.ppm; *.pgm; *.pbm)')
                if imagemSalvaComo:
                    self.parts = imagemSalvaComo.rpartition('/')
                    self.enderecoSalvo = self.parts[0]
                    if self.endImagemResultado != '':
                        shutil.move(self.endImagemResultado, self.enderecoSalvo + '/' +
                                   os.path.splitext(os.path.basename(imagemSalvaComo))[0] +
                                   self.extensaoImagemResultado)
                    else:
                        shutil.copyfile(self.endImagemOriginal, self.enderecoSalvo + '/' +
                                        os.path.splitext(os.path.basename(imagemSalvaComo))[0] +
                                        self.extensaoImagemOriginal)
        except:
            pass

    def procurarImagemTransformadaNaoSalva(self):
        return os.path.exists(self.imagemResultado + self.extensaoImagemResultado)


    def excluirCopiaImgTransformada(self):
        try:
            if os.path.exists(self.imagemResultado + "Copia" + '.ppm'):
                os.remove(self.imagemResultado + "Copia" + '.ppm')

            if os.path.exists(self.imagemResultado + "Copia" + '.pgm'):
                os.remove(self.imagemResultado + "Copia" + '.pgm')

            if os.path.exists(self.imagemResultado + "Copia" + '.pbm'):
                os.remove(self.imagemResultado + "Copia" + '.pbm')

        except:
            pass

    def excluirImagemTransformadaNaoSalva(self):
        try:
            if os.path.exists(self.imagemResultado + '.ppm'):
                os.remove(self.imagemResultado + '.ppm')

            if os.path.exists(self.imagemResultado + '.pgm'):
                os.remove(self.imagemResultado + '.pgm')

            if os.path.exists(self.imagemResultado + '.pbm'):
                os.remove(self.imagemResultado + '.pbm')
        except:
            pass
