# *-* coding: utf:8 -*-

import sys
import numpy as np


def lerImagemEntrada():
    entrada = open(sys.argv[1], "r+")

    linha = entrada.readline()  # Tipo
    linha = entrada.readline()  # Comentário
    linha = entrada.readline()  # Dimensões da imagem
    dimensoes = linha.split()
    largura = int(dimensoes[0])
    altura = int(dimensoes[1])
    linha = entrada.readline() #Valor fixo
    linha = entrada.readlines()

    # converter de lista para array
    imagem = np.asarray(linha, dtype=int)
    imagem = np.reshape(imagem, (altura, largura, 3))

    escreverImagemSaida(entrada, largura, altura, imagem)


def escreverImagemSaida(entrada, largura, altura, imagem):
    saida = open(sys.argv[2], "w+")
    saida.write("P3\n")
    saida.write("#Criado por Luiz\n")
    saida.write(str(largura))
    saida.write(" ")
    saida.write(str(altura))
    saida.write("\n")
    saida.write("255\n")

    # remover canal Azul da imagem
    for i in range(0, len(imagem)):
        for j in range(0, len(imagem[1])):
            r = imagem[i][j][0]
            g = imagem[i][j][1]
            b = 0
            saida.write(str(r))
            saida.write("\n")
            saida.write(str(g))
            saida.write("\n")
            saida.write(str(b))
            saida.write("\n")

    # fechar os arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    lerImagemEntrada()
