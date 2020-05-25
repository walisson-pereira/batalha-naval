class Matriz:

    def __init__(self, linha=10, coluna=0, valor_padrao=0):
        if coluna == 0:
            coluna = linha

        self._matriz = []

        for lin in range(linha):
            linha_da_matriz = []
            for col in range(coluna):
                linha_da_matriz.append(valor_padrao)
            self._matriz.append(linha_da_matriz)

    def __str__(self):
        retorno = ''
        for lin in range(self.linha):
            for col in range(self.coluna):
                if col == 0:
                    retorno += str(self._matriz[lin][col])
                else:
                    retorno += ' ' + str(self._matriz[lin][col])
            retorno += '\n'
        return retorno

    @property
    def linha(self) -> int:
        return len(self._matriz)

    @property
    def coluna(self) -> int:
        return len(self._matriz[0])

    def set(self, linha: int, coluna: int, valor) -> None:
        self._matriz[linha][coluna] = valor

    def get(self, linha: int, coluna: int):
        return self._matriz[linha][coluna]

    def tem(self, elemento) -> bool:
        for lin in range(self.linha):
            for col in range(self.coluna):
                if self._matriz[lin][col] == elemento:
                    return True
        return False
