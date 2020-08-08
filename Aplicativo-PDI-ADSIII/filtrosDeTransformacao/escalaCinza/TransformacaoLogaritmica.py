# *-* coding: utf:8 -*-

'''A transformação logarítmica realce os tons escuros da imagem.
Isso acontece porque ela mapeia uma faixa estreita de valores escuros na imagem de
entrada em uma faixa mais ampla na imagem de saída, tornando a imagem mais clara'''

import sys
import numpy as np
import math


def lerImagemEntrada():
    entrada = open(sys.argv[1], "r+")

    linha = entrada.readline() # Tipo
    linha = entrada.readline() # Comentário
    linha = entrada.readline() # Dimensões
    dimensoes = linha.split()
    largura = dimensoes[0]
    altura = dimensoes[1]
    linha = entrada.readline() # Valor fixo
    linha = entrada.readlines()

    imagem = np.asarray(linha, dtype=int)

    escreverImagemSaida(entrada, largura, altura, imagem)


def escreverImagemSaida(entrada, largura, altura, imagem):
    saida = open(sys.argv[2], "w+")
    saida.write("P2\n")
    saida.write("#Criado por Luiz\n")
    saida.write(str(largura))
    saida.write(" ")
    saida.write(str(altura))
    saida.write("\n")
    saida.write("255\n")

    #fazer a transformação de intesidade (negativo)
    for i in range((len(imagem))):
        n = int((math.log(1 + (imagem[i]/255)))*255)
        n = str(n)
        saida.write(n)
        saida.write("\n")

    # fechar os arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    lerImagemEntrada()
