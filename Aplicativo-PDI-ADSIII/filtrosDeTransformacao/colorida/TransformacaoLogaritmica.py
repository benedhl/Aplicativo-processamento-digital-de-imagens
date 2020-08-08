# *-* coding: utf:8 -*-

import sys
import numpy as np
import math


def lerImagemEntrada():
    entrada = open(sys.argv[1], "r+")

    linha = entrada.readline()  # Tipo
    linha = entrada.readline()  # Comentário
    linha = entrada.readline()  # Dimensões
    dimensoes = linha.split()
    largura = int(dimensoes[0])
    altura = int(dimensoes[1])
    linha = entrada.readline()  # Valor fixo
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

    # aplicar transformação logarítmica na imagem
    for i in range(len(imagem)):
        for j in range(len(imagem[1])):
            for k in range(3):
                sum = int((math.log(1 + (imagem[i][j][k] / 255))) * 255)
                sum = str(sum)
                saida.write(sum)
                saida.write("\n")

    # fechar os arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    lerImagemEntrada()
