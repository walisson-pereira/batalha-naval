from batalha import BatalhaNaval

b = BatalhaNaval(player=1)

b.adicione_um_navio(0,0,3,False)

b.ataque_inimigo(2,0)
print(b)

