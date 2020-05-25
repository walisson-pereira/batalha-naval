from batalha import BatalhaNaval

b = BatalhaNaval(player=2)

b.adicione_um_navio(1,0,3,False)

b.receba_ataque()
b.receba_ataque()
b.receba_ataque()
b.receba_ataque()

#input('aperte qualquer coisa')
print(b)


