class ControleChecagemFiltros():
    def __init__(self, ):
        super(ControleChecagemFiltros, self).__init__()
        self.listaFiltrosUsados = []

    '''Contolar quais submenus e actions estão visíveis dependendo do tipo da imagem'''

    def removerChecagemFiltrosUsados(self):
        for filtro in self.listaFiltrosUsados:
            filtro.setChecked(False)

        self.listaFiltrosUsados.clear()
