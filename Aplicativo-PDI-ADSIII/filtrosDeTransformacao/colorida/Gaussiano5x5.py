# *-* coding: utf:8 -*-

import sys
import numpy as np


def lerImagemEntrada():
    entrada = open(sys.argv[1], "r+")

    linha = entrada.readline() # Tipo
    linha = entrada.readline() # Comentário
    linha = entrada.readline() # Dimensões
    dimensoes = linha.split()
    linha = entrada.readline() # Valor Fixo
    dimensoes = np.array(dimensoes, dtype=int)

    linhas = entrada.readlines()
    imagem = np.array(list(linhas))
    imagem = np.reshape(imagem, [dimensoes[1], dimensoes[0], 3])
    imagem = imagem.astype(int)

    # Matriz Filtro Gaussiano 5x5
    kernel = [[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4], [1, 4, 7, 4, 1]]
    kernel = np.asarray(kernel)/273

    ks = int((len(kernel) - 1) / 2)

    escreverImagemSaida(entrada, dimensoes, imagem, kernel, ks)


def escreverImagemSaida(entrada, dimensoes, imagem, kernel, ks):
    saida = open(sys.argv[2], "w+")
    saida.write('P3\n')
    saida.write('#Criado por Luiz\n')
    largura = dimensoes[0]
    altura = dimensoes[1]
    saida.write(str(largura-(ks*2)))
    saida.write(' ')
    saida.write(str(altura-(ks*2)))
    saida.write('\n')
    saida.write('255\n')

    # aplicar filtro gaussiano na imagem
    for i in range(ks, len(imagem)-ks):
        for j in range(ks, len(imagem[1])-ks):
            for k in range(3):
                sum = 0
                for ki in range(len(kernel)):
                    for kj in range(len(kernel[1])):
                            sum = sum + (imagem[i - ks + ki][j - ks + kj][k] * kernel[ki][kj])
                sum = int(sum)
                sum = str(sum)
                saida.write(sum)
                saida.write("\n")

    # fechar os arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    lerImagemEntrada()
