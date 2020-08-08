# *-* coding: utf:8 -*-

'''A negativa de uma imagem é obtida ao inverter-se a intensidade luminosa de todos
os pontos da imagem, resultando em uma nova imagem com aspecto semelhante a um negativo fotográfico '''

import sys
import numpy as np


def lerImagemEntrada():
    entrada = open(sys.argv[1], "r+")

    # Fazer o Processamento Digital de Imagens
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
    saida.write('P3\n')
    saida.write('#Criado por Luiz\n')
    largura = dimensoes[0]
    altura = dimensoes[1]
    saida.write(str(largura))
    saida.write(' ')
    saida.write(str(altura))
    saida.write('\n')
    saida.write('255\n')

    # aplicar filtro negativo na imagem
    for i in range(len(imagem)):
        for j in range(len(imagem[1])):
            for k in range(3):
                sum = 255 - imagem[i][j][k]
                sum = str(sum)
                saida.write(sum)
                saida.write("\n")

    # fechar os arquivos
    entrada.close()
    saida.close()


if __name__ == "__main__":
    lerImagemEntrada()
