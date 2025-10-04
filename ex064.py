n = 0
s = 0
q = 0

while n != 999:
    n = int(input('digite um numero: '))
    q += 1
    s += n

print('a quantidade de numeros digitados foi de {}'.format(q - 1))
print('a soma dos numeros: {}'.format(s - 999))