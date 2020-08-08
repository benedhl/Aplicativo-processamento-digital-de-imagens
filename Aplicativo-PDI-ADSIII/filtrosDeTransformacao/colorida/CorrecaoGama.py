# *-* coding: utf:8 -*-

import sys
import numpy as np

'''Gama ou correção de gama é uma operação não-linear que é usada para codificar e decodificar luminância ou valores 
de cores em imagem. Ela é usada em muitos tipos de sistemas de imagem para endireitar uma resposta curva de 
sinal-para-luz ou deintensidade-para-sinal. O Gama é usado como um expoente (potência) na equação de correção'''


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

    escreverImagemSaida(entrada, dimensoes, imagem)


def escreverImagemSaida(entrada, dimensoes, imagem):
    saida = open(sys.argv[2], "w+")
    saida.write("P3\n")
    saida.write("#Criado por Luiz\n")
    largura = dimensoes[0]
    altura = dimensoes[1]
    saida.write(str(largura))
    saida.write(" ")
    saida.write(str(altura))
    saida.write("\n")
    saida.write("255\n")
    # valor fator gamma
    gamma = float(sys.argv[3])

    # calcular a correção gama sobre a imagem
    for i in range(len(imagem)):
        for j in range(len(imagem[1])):
            for k in range(3):
                n = int(((imagem[i][j][k] / 255) ** gamma) * 255)
                n = str(n)
                saida.write(n)
                saida.write("\n")

    # fechar os arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    lerImagemEntrada()
