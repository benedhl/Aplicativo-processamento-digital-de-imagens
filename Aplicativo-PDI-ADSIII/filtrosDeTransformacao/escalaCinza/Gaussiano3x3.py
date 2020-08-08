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

    imagem = np.asarray(linha, dtype=int)
    imagem = np.reshape(imagem, (altura, largura))

    # Matriz Filtro Gaussiano 3x3
    kernel = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    kernel = np.asarray(kernel) / 16

    ks = int((len(kernel) - 1) / 2)

    escreverImagemSaida(entrada, largura, altura, imagem, kernel, ks)


def escreverImagemSaida(entrada, largura, altura, imagem, kernel, ks):
    saida = open(sys.argv[2], "w+")
    saida.write("P2\n")
    saida.write("#Criado por Luiz\n")
    saida.write(str(largura-(ks*2)))
    saida.write(" ")
    saida.write(str(altura-(ks*2)))
    saida.write("\n")
    saida.write("255\n")

    # aplicar filtro gaussiano na imagem
    for i in range(ks, len(imagem)-ks):
        for j in range(ks, len(imagem[1])-ks):
            sum = 0
            for ki in range(len(kernel)):
                for kj in range(len(kernel[1])):
                    sum = sum + (imagem[i - ks + ki][j - ks + kj] * kernel[ki][kj])
            sum = int(sum)
            sum = str(sum)
            saida.write(sum)
            saida.write("\n")

    # fechar os arquivos
    entrada.close()
    saida.close()

if __name__ == "__main__":
    lerImagemEntrada()
