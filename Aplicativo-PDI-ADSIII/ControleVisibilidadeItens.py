class ControleVisibilidadeItens():
    def __init__(self, opcaoInfoImagem, opcaoSalvarComo):
        super(ControleVisibilidadeItens, self).__init__()
        '''Controle de visibilidade'''
        self.opcaoInfoImagem = opcaoInfoImagem
        self.opcaoSalvarComo = opcaoSalvarComo
        self.listaFiltrosImgColoridaCinza = []
        self.listaFiltrosImgPretoBranco = []
        self.listaRemoverFiltrosParaEscalaDeCinza = []

    def alterarVisibilidadeItensMenuTransformacoes(self, extensao):

        self.opcaoInfoImagem.setVisible(True)
        self.opcaoSalvarComo.setDisabled(False)

        if extensao == '.ppm':
            for filtro in self.listaFiltrosImgColoridaCinza:
                filtro.setDisabled(False)

            for filtro in self.listaFiltrosImgPretoBranco:
                if filtro not in self.listaFiltrosImgColoridaCinza:
                    filtro.setDisabled(True)

        elif extensao == '.pgm':
            for filtro in self.listaFiltrosImgColoridaCinza:
                if filtro in self.listaRemoverFiltrosParaEscalaDeCinza:
                    filtro.setDisabled(True)
                else:
                    filtro.setDisabled(False)

            for filtro in self.listaFiltrosImgPretoBranco:
                if filtro not in self.listaFiltrosImgColoridaCinza:
                    filtro.setDisabled(True)

        elif extensao == '.pbm':
            for filtro in self.listaFiltrosImgColoridaCinza:
                filtro.setDisabled(True)

            for filtro in self.listaFiltrosImgPretoBranco:
                filtro.setDisabled(False)
