from utils.matriz import Matriz


class MatrizDupla:

    def __init__(self, linha: int, coluna: int, valor_padrao=0):
        self._principal = Matriz(linha, coluna, valor_padrao)
        self._secundaria = Matriz(linha, coluna, valor_padrao)

    def __str__(self):
        retorno = '  '
        for lin in range(self.linha):
            retorno += ' {:02}'.format(lin)
        retorno += ' | '
        for lin in range(self.linha):
            retorno += ' {:02}'.format(lin)
        retorno += '\n'
        for lin in range(self.linha):
            for col in range(self.coluna):
                if col == 0:
                    retorno += '{:02} '.format(lin) + ' ' + str(self._principal.get(lin, col))
                else:
                    retorno += '  ' + str(self._principal.get(lin, col))
            retorno += ' | '
            for col in range(self.coluna):
                retorno += '  ' + str(self._secundaria.get(lin, col))
            retorno += '\n'
        return retorno

    @property
    def linha(self):
        return self._principal.linha

    @property
    def coluna(self):
        return self._principal.coluna

    def set(self, matriz, linha, coluna, valor) -> None:
        if matriz == 0 or matriz == 'principal':
            self._principal.set(linha, coluna, valor)
        else:
            self._secundaria.set(linha, coluna, valor)

    def get(self, matriz, linha, coluna):
        if matriz == 0 or matriz == 'principal':
            return self._principal.get(linha, coluna)
        return self._secundaria.get(linha, coluna)
