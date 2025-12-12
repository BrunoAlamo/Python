m = 0
f = 0
mi = 0
maior = 0
h = []
li = []
am = []

for c in range(1, 5):
    n = str(input('digite o seu nome: '))
    i = int(input('digite a sua idade: '))
    s = int(input('digite 1 para sexo masculino e 2 para feminino: '))
    mi += i / 4
    if s == 2 and i < 20:
        f += 1
    if s == 1:
        h.append(n)
        li.append(i)
    if c == 1:
        maior = i
    else:
        if i > maior:
            maior = i


for y in range(0, len(h)):
    if li[y] == maior:
        am.append(h.pop(y))


print('a média de idade do grupo é de {} anos'.format(mi))
print('o homem com maior idade é {}'.format(am[0]))
print('o número de mulheres com menos de 20 anos é {}'.format(f))