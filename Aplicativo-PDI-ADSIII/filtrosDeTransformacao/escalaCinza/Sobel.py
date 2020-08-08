# *-* coding: utf:8 -*-

'''
O filtro Sobel detecta bordas horizontais e verticais separadamente em uma imagem em escalas-de-cinza.
As cores da imagem são transformadas de RGB para escalas-de-cinza.
O resultado é uma imagem transparente com linhas pretas e alguns restos de cores.'''

import sys
import numpy as np
import math


def lerImagemEntrada():
    entrada = open(sys.argv[1], "r+")

    linha = entrada.readline()  # Tipo
    linha = entrada.readline()  # Comentário
    linha = entrada.readline()  # Dimensões da imagem
    dimensoes = linha.split()
    largura = int(dimensoes[0])
    altura = int(dimensoes[1])
    linha = entrada.readline()  # Valor fixo
    linha = entrada.readlines()

    imagem = np.asarray(linha, dtype=int)
    imagem = np.reshape(imagem, (altura, largura))

    # Matrizes filtro Sobel
    kernelx = [[-1, 0, 1], [2, 0, -2], [1, 0, -1]]
    kernelx = np.asarray(kernelx)
    kernely = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    kernely = np.asarray(kernely)
    ks = int((len(kernelx) - 1) / 2)
    threshold = int(sys.argv[3])

    escreverImagemSaida(entrada, largura, altura, imagem, kernelx, kernely, ks, threshold)


def escreverImagemSaida(entrada, largura, altura, imagem, kernelx, kernely, ks, threshold):
    saida = open(sys.argv[2], "w+")
    saida.write("P2\n")
    saida.write("#Criado por Luiz\n")
    saida.write(str(largura - (ks * 2)))
    saida.write(" ")
    saida.write(str(altura - (ks * 2)))
    saida.write("\n")
    saida.write("255\n")

    # aplicar filtro sobel
    for i in range(ks, len(imagem) - ks):
        for j in range(ks, len(imagem[1]) - ks):
            sumx = 0
            sumy = 0
            for ki in range(len(kernelx)):
                for kj in range(len(kernelx[1])):
                    sumx = sumx + (imagem[i - ks + ki][j - ks + kj] * kernelx[ki][kj])
                    sumy = sumy + (imagem[i - ks + ki][j - ks + kj] * kernely[ki][kj])
            sumxy = math.sqrt((sumx ** 2) + (sumy ** 2))
            # Threshold
            sum = max(sumxy, threshold)
            sum = int(sum) if sum != threshold else 0
            sum = str(sum)
            saida.write(sum)
            saida.write("\n")

    # fechar os dois arquivos.
    entrada.close()
    saida.close()


if __name__ == "__main__":
    lerImagemEntrada()
