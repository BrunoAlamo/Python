from random import randint

j = {}
d = 0
maior = 0
menor = 0
o = {}
print('Valores Sorteados: ')
for c in range(1, 5):
    d = randint(1, 6)
    print(f'o jogador {c} tirou {d} no dado')
    j[f'jogador{c}'] = d
    if c == 1:
        maior = menor = j[f'jogador{c}']
    else:
        if j[f'jogador{c}'] > maior:
            maior = j[f'jogador{c}']
        elif j[f'jogador{c}'] < menor:
            menor = j[f'jogador{c}']
print(maior)
print(menor)
print('Ranking dos jogadores: ')
for k, v in j.items():
    if v == maior:
        print(f'{k} com {v}')

for k, v in j.items():
    if menor < v < maior:
        print(f'{k} com {v}')

for k, v in j.items():
    if v == menor:
        print(f'{k} com {v}')