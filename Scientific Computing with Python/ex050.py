s = 0

for c in range(0, 6):
    i = int(input('digite um numero inteiro: '))
    if i % 2 == 0:
        s += i
print('a soma dos numeros inteiro pares: {}'.format(s))