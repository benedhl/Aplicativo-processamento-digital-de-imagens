# -*- coding: utf-8 -*-

'''Gama ou correção de gama é uma operação não-linear que é usada para codificar e decodificar luminância ou valores
de cores em imagem. Ela é usada em muitos tipos de sistemas de imagem para endireitar uma resposta curva de
sinal-para-luz ou deintensidade-para-sinal. O Gama é usado como um expoente (potência) na equação de correção'''

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
    # fator gama
    gama = float(sys.argv[3])

    # aplicar correção gama
    for i in range((len(imagem))):
        n = int(((imagem[i]/255)**gama)*255)
        n = str(n)
        saida.write(n)
        saida.write("\n")

    # fechar os dois arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    lerImagemEntrada()