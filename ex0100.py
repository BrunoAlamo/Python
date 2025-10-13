from random import randint
from time import sleep

v = []

def sorteia():
    print(f'sorteando 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        r = randint(1, 10)
        v.append(r)
        print(r, end=' ')
        sleep(0.3)
    print()

def somapar():
    print(f'somando os valores pares da lista: {v}, temos ', end='')
    s = 0
    for c in v:
        if c % 2 == 0:
            s += c
    print(s)


sorteia()
somapar()