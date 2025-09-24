import random

print('vamos jogar JOKENPO')
u = input('digite 1 para PEDRA, 2 para PAPEL e 3 para TESOURA: ')
jogadas = ('PEDRA', 'PAPEL', 'TESOURA')
r = random.randint(1, 3)

if u == '1' and r == 1:
    print('minha jogada: {}'.format(jogadas[r-1]))
    print('EMPATE!')
elif u == '2' and r == 1:
    print('minha jogada: {}'.format(jogadas[r-1]))
    print('VOCÊ VENCEU!')
elif u == '3' and r == 1:
    print('minha jogada: {}'.format(jogadas[r-1]))
    print('VOCÊ PERDEU!')
elif u == '1' and r == 2:
    print('minha jogada: {}'.format(jogadas[r-1]))
    print('VOCÊ PERDEU!')
elif u == '2' and r == 2:
    print('minha jogada: {}'.format(jogadas[r-1]))
    print('EMPATE!')
elif u == '3' and r == 2:
    print('minha jogada: {}'.format(jogadas[r-1]))
    print('VOCÊ VENCEU!')
elif u == '1' and r == 3:
    print('minha jogada: {}'.format(jogadas[r-1]))
    print('VOCÊ VENCEU!')
elif u == '2' and r == 3:
    print('minha jogada: {}'.format(jogadas[r-1]))
    print('VOCÊ PERDEU!')
elif u == '3' and r == 3:
    print('minha jogada: {}'.format(jogadas[r-1]))
    print('EMPATE!')