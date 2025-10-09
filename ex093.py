j = {}

n = str(input('Nome do jogador: '))
j['nome'] = n
p = int(input(f'Quantas partidas {n} jogou? '))
c = 0
j['gols'] = []
t = 0
while p != c:
    g = int(input(f'quantos gols na partida {c}? '))
    j['gols'].append(g)
    t += g
    c += 1
j['total'] = t
print('-=' * 30)
print(j)
print('-=' * 30)
for k, v in j.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {n} jogou {p} partidas.')
for c in range(0, p):
    print(f'=> na partida {c}, fez {j["gols"][c]} gols')
print(f'Foi um total de {t} gols.')

