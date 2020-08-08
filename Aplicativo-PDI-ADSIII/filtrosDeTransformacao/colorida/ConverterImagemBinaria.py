# *-* coding: utf:8 -*-

import sys
import numpy as np


def lerImagemEntrada():
    entrada = open(sys.argv[1], "r+")

    linha = entrada.readline() # Tipo
    linha = entrada.readline() # Comentário
    linha = entrada.readline() # Dimensões
    dimensoes = linha.split()
    largura = int(dimensoes[0])
    altura = int(dimensoes[1])
    linha = entrada.readline() # Valor fixo
    linha = entrada.readlines()

    imagem = np.asarray(linha, dtype=int)
    imagem = np.reshape(imagem, (altura, largura, 3))
    linhas = converterParaEscalaDeCinza(imagem)
    # converter de lista para array
    imagem = np.asarray(linhas, dtype=int)
    imagem = np.reshape(imagem, (altura, largura))

    escreverImagemSaida(entrada, largura, altura, imagem)

def converterParaEscalaDeCinza(imagem):
    linhas = []

    # converter pixels coloridos para escala de cinza
    for i in range(len(imagem)):
        for j in range(len(imagem[1])):
            sum = 0
            for k in range(3):
                sum = sum + imagem[i][j][k]
            sum = int(sum / 3)
            sum = str(sum)
            linhas.append(sum)
    return linhas


def escreverImagemSaida(entrada, largura, altura, imagem):
    saida = open(sys.argv[2], "w+")
    saida.write("P1\n")
    saida.write("#Criado por Luiz\n")
    saida.write(str(largura))
    saida.write(" ")
    saida.write(str(altura))
    saida.write("\n")
    limite = int(sys.argv[3])

    # fazer a cópia para imagem binária
    for i in range(len(imagem)):
        for j in range(len(imagem[1])):
            if imagem[i][j] > limite:
                saida.write("0")
            else:
                saida.write("1")
            saida.write("\n")

    # fechar os arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    lerImagemEntrada()
