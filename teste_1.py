from batalha import BatalhaNaval

b = BatalhaNaval(player=1)

b.adicione_um_navio(0, 0, 3, False)

b.ataque_inimigo(1, 0)
b.ataque_inimigo(1, 1)
b.ataque_inimigo(7, 2)
b.ataque_inimigo(1, 2)

print(b)
