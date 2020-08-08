import os
import shutil
import subprocess

from PyQt5.QtGui import QPixmap


class TransformacaoImagens():
    def __init__(self, manipulacaoImagens, barraProgresso, barraStatus):
        super(TransformacaoImagens, self).__init__()
        self.manipulacaoImagens = manipulacaoImagens
        self.barraProgresso = barraProgresso
        self.barraStatus = barraStatus

    def transformarImagem(self, filtro, script, extensao, valorArgumento3):

        porcentagemProgresso = 0
        self.barraProgresso.setValue(porcentagemProgresso)
        self.filtroUsado = ''

        if os.path.exists(self.manipulacaoImagens.imagemResultado + "Copia" +
                          self.manipulacaoImagens.extensaoImagemResultado):

            self.imagemEntrada = self.manipulacaoImagens.imagemResultado + "Copia" + \
                                 self.manipulacaoImagens.extensaoImagemResultado
        else:
            self.imagemEntrada = self.manipulacaoImagens.endImagemOriginal

        try:
            if self.manipulacaoImagens.extensaoImagemOriginal == '.ppm':
                self.script = 'filtrosDeTransformacao/colorida/' + script + '.py'
                self.manipulacaoImagens.extensaoImagemResultado = extensao
                self.filtroUsado = filtro

            elif self.manipulacaoImagens.extensaoImagemOriginal == '.pgm':
                self.script = 'filtrosDeTransformacao/escalaCinza/' + script + '.py'
                self.manipulacaoImagens.extensaoImagemResultado = extensao
                self.filtroUsado = filtro

            elif self.manipulacaoImagens.extensaoImagemOriginal == '.pbm':
                self.script = 'filtrosDeTransformacao/pretoBranco/' + script + '.py'
                self.manipulacaoImagens.extensaoImagemResultado = extensao
                self.filtroUsado = filtro

            self.argumentos = 'python ' + self.script + ' \"' + self.imagemEntrada + '\" ' + \
                              self.manipulacaoImagens.imagemResultado + self.manipulacaoImagens.extensaoImagemResultado \
                              + ' \" ' + valorArgumento3

            self.executarTransformacao = subprocess.run(self.argumentos, shell=True)

            while porcentagemProgresso < 100:
                if self.executarTransformacao is not None:
                    porcentagemProgresso += 0.001
                    self.barraProgresso.setValue(int(porcentagemProgresso))
                else:
                    break

            self.manipulacaoImagens.endImagemResultado = self.manipulacaoImagens.imagemResultado + \
                                      self.manipulacaoImagens.extensaoImagemResultado
            self.manipulacaoImagens.pixmapImagem = QPixmap(self.manipulacaoImagens.endImagemResultado)
            shutil.copyfile(self.manipulacaoImagens.endImagemResultado, self.manipulacaoImagens.imagemResultado +
                            "Copia" + self.manipulacaoImagens.extensaoImagemResultado)
            self.manipulacaoImagens.exibirImagem()
            self.manipulacaoImagens.controleChecagemFiltros.listaFiltrosUsados.append(self.filtroUsado)
            self.manipulacaoImagens.extensaoImagemOriginal = self.manipulacaoImagens.extensaoImagemResultado

            self.barraStatus.showMessage("Você aplicou o  " + filtro.text().replace("&", ""), 5000)

            porcentagemProgresso = 0
            self.barraProgresso.setValue(porcentagemProgresso)

        except:
            pass
