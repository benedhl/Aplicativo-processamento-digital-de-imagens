# *-* coding: utf:8 -*-
import numpy as np
import sys

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
        n = 255 - imagem[i]
        n = str(n)
        saida.write(n)
        saida.write("\n")


    # fechar os arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    lerImagemEntrada()
