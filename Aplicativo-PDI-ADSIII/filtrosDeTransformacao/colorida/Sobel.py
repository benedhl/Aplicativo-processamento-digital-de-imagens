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
    linha = entrada.readline()  # Dimensões
    dimensoes = linha.split()
    linha = entrada.readline()  # Valor Fixo
    dimensoes = np.array(dimensoes, dtype=int)

    linhas = entrada.readlines()
    imagem = np.array(list(linhas))
    imagem = np.reshape(imagem, [dimensoes[1], dimensoes[0], 3])
    imagem = imagem.astype(int)

    # Matrizes filtro Sobel
    kernelx = [[-1, 0, 1], [2, 0, -2], [1, 0, -1]]
    kernelx = np.asarray(kernelx)
    kernely = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    kernely = np.asarray(kernely)
    ks = int((len(kernelx) - 1) / 2)
    threshold = int(sys.argv[3])

    escreverImagemSaida(entrada, dimensoes, imagem, kernelx, kernely, ks, threshold)


def escreverImagemSaida(entrada, dimensoes, imagem, kernelx, kernely, ks, threshold):
    saida = open(sys.argv[2], "w+")
    saida.write('P3\n')
    saida.write('#Criado por Luiz\n')
    largura = dimensoes[0]
    altura = dimensoes[1]
    saida.write(str(largura - (ks * 2)))
    saida.write(' ')
    saida.write(str(altura - (ks * 2)))
    saida.write('\n')
    saida.write('255\n')

    # aplicar filtro sobel
    for i in range(ks, len(imagem) - ks):
        for j in range(ks, len(imagem[1]) - ks):
            for k in range(3):
                sumx = 0
                sumy = 0
                for ki in range(len(kernelx)):
                    for kj in range(len(kernelx[1])):
                        sumx = sumx + (imagem[i - ks + ki][j - ks + kj][k] * kernelx[ki][kj])
                        sumy = sumy + (imagem[i - ks + ki][j - ks + kj][k] * kernely[ki][kj])
                sumxy = math.sqrt((sumx ** 2) + (sumy ** 2))
                # aplicando valor Threshold escolhido pelo usuário
                sum = max(sumxy, threshold)
                sum = int(sum) if sum != threshold else 0
                print(sum)
                sum = str(sum)
                saida.write(sum)
                saida.write("\n")

    # fechar os arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    lerImagemEntrada()
