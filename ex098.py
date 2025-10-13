from time import sleep

def cont(i, f, p):
    if f < i and p > 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'contagem de {i} até {f} de {p} em {p}')
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.5)


print('-=' * 30)
print('Contagem de 1 a 10, de 1 em 1')
for c in range(1, 11, 1):
    print(c, end=' ')
    sleep(0.5)
print()
print('-=' * 30)
print('Contagem de 10 até 0 de 2 em 2')
for c in range(10, -1, -2):
    print(c, end=' ')
    sleep(0.5)
print()
print('-=' * 30)
print('Agora é sua vez de persnalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('-=' * 30)
cont(i, f, p)
print()
print('FIM!')