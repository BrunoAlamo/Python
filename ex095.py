j = {}
l = []
while True:
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
    l.append(j)
    j = {}
    while True:
        s = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if s == 'S' or s == 'N':
            break
    if s == 'N':
        break

print('-=' * 30)
print(l)
print('-=' * 30)
print('cod    nome    gols     total')
for h in range(0, len(l)):
    print(f'{h:^5}', end=' ')
    for k, v in l[h].items():
        print(f'{v}', end=' ')
    print()
print()
print('-=' * 30)
d = 0
y = 0
while d != 999:
    d = int(input('Quer mostrar os dados de qual jogador? '))
    print(f'-- Mostrando os dados do jogador {l[d]["nome"]}')
    for f in l[d]["gols"]:
        print(f'no jogo {y} fez {f} gols')
        y += 1


