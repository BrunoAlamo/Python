n = 0
c = 0
q = 0
m = 0
maior = 0
menor = 0

while c != 2:
    n = int(input('digite um numero: '))
    c = int(input('digite 1 para continuar e 2 parar sair do programa: '))
    q += 1
    m += n
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('a media entre todos os valores digitados foi de {}'.format(m / q))
print('o maior valor digitado foi de {}'.format(maior))
print('o menor valor digitado foi de {}'.format(menor))