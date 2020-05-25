from utils.matriz_dupla import MatrizDupla
from utils.comunicador import Comunicador



class BatalhaNaval:
    MAR = '~'
    BOMBA_ERRO = '*'
    BOMBA_ACERTO = '@'
    NAVIO = 'O'
    BOMBA_RECEBIDA = '*'
    PORT_PLAYER_1 = 65432
    PORT_PLAYER_2 = 65433

    def __init__(self, player=1):
        self._oceano = MatrizDupla(valor_padrao=BatalhaNaval.MAR)
        self.player = int(player)

    def __str__(self):
        return str(self._oceano)

    def fim_de_jogo(self):
        return not (self._oceano.tem_no_principal(BatalhaNaval.NAVIO))

    def adicione_um_navio(self, linha: int, coluna: int, tamanho: int, horizontal=True) -> bool:
        try:
            if horizontal:
                linha_inicio = linha
                linha_fim = linha + tamanho
                coluna_inicio = coluna
                coluna_fim = coluna + 1
            else:
                linha_inicio = linha
                linha_fim = linha + 1
                coluna_inicio = coluna
                coluna_fim = coluna + tamanho

            # verificar se está dentro da faixa aceitável
            if not (0 <= linha_inicio < self._oceano.linha and
                    0 <= linha_fim - 1 < self._oceano.linha and
                    0 <= coluna_inicio < self._oceano.coluna and
                    0 <= coluna_fim - 1 < self._oceano.coluna):
                return False

            for lin in range(linha_inicio, linha_fim):
                for col in range(coluna_inicio, coluna_fim):
                    self._oceano.set('principal', lin, col, BatalhaNaval.NAVIO)

        except IndexError:
            return False
        return True

    def adicione_navios(self, quantidades=[2, 3, 3]) -> bool:
        cont = 0
        total = len(quantidades)
        while cont < total:
            tamanho = quantidades[cont]
            print('Adicionando navio {}/{}'.format(cont, total))
            linha = int(input('Qual a linha (0-{:2})? '.format(self._oceano.linha - 1)))
            coluna = int(input('Qual a coluna (0-{:2}? '.format(self._oceano.coluna - 1)))
            orientacao = input('Vertical ou Horizontal (v|h)?')
            horizontal = True
            if orientacao == 'v' or orientacao == 'V':
                horizontal = False
            deu_certo = self.adicione_um_navio(linha, coluna, tamanho, horizontal)
            if not deu_certo:
                return False
            cont += 1
        return True

    def ataque_inimigo(self, linha, coluna) -> bool:
        mensagem = 'ATAQUE {} {}'.format(linha, coluna)
        if self.player == 1:
            Comunicador.envie_mensagem(mensagem, port=BatalhaNaval.PORT_PLAYER_2)
            resposta = Comunicador.receba_mensagem(port=BatalhaNaval.PORT_PLAYER_2)
        else:
            Comunicador.envie_mensagem(mensagem, port=BatalhaNaval.PORT_PLAYER_1)
            resposta = Comunicador.receba_mensagem(port=BatalhaNaval.PORT_PLAYER_2)

        if resposta == 'ACERTO':
            self.registra_acerto(linha, coluna)
        else:
            self.registra_erro(linha, coluna)

        if self.player == 1:
            resposta = Comunicador.receba_mensagem(port=BatalhaNaval.PORT_PLAYER_2)
        else:
            resposta = Comunicador.receba_mensagem(port=BatalhaNaval.PORT_PLAYER_1)
        print('Recebido a mensagem:\n')
        print(resposta)
        if resposta == 'FIM':
            print('Fim do jogo! Você ganhou!')
            exit()
        return True

    def receba_ataque(self) -> bool:
        if self.player == 1:
            mensagem = Comunicador.receba_mensagem(port=BatalhaNaval.PORT_PLAYER_1)
        else:
            mensagem = Comunicador.receba_mensagem(port=BatalhaNaval.PORT_PLAYER_2)
        print('mensagem recebida:\n')
        print(mensagem)
        if mensagem.split()[0] == 'ATAQUE':
            print('Recebi um ataque')
            linha = int(mensagem.split()[1])
            coluna = int(mensagem.split()[2])
            self.registra_bomba_recebida(linha, coluna)
            perdeu = self.fim_de_jogo()
            if perdeu:
                mensagem = 'FIM'
                print('Fim de jogo! Você perdeu!')
            else:
                mensagem = 'NÃO'

            if self.player == 1:
                Comunicador.envie_mensagem(mensagem, port=BatalhaNaval.PORT_PLAYER_2)
            else:
                Comunicador.envie_mensagem(mensagem, port=BatalhaNaval.PORT_PLAYER_1)
        return True

    def registra_acerto (self, linha: int, coluna: int):
        self._oceano.set('secundario', linha, coluna, BatalhaNaval.BOMBA_ACERTO)

    def registra_erro(self, linha: int, coluna: int):
        self._oceano.set('secundario', linha, coluna, BatalhaNaval.BOMBA_ERRO)

    def registra_bomba_recebida (self, linha: int, coluna: int):
        self._oceano.set('principal', linha, coluna, BatalhaNaval.BOMBA_RECEBIDA)
