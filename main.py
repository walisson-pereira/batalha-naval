from batalha import BatalhaNaval
import os

print('Jogo de Batalha Naval')
player = int(input('Este é o jogador 1 ou 2? '))
b = BatalhaNaval(player=player)

print('Vamos adicionar seus navios')
b.adicione_navios()

input('Aperte enter para continuar')

while True:
    os.system('clear')
    if player != 1:
        b.receba_ataque()
    print('Mapa atual')
    print(b)
    print('Hora do ataque:')
    linha = int(input('Digite a linha (0 - 9): '))
    coluna = int(input('Digite a coluna (0 - 9): '))
    b.ataque_inimigo(linha, coluna)
    if player == 1:
        b.receba_ataque()