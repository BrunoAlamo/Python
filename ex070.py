t = 0
c = 0
m = 0
r = 0
b = []
pa = []


while True:
    n = str(input('digite o nome do produto: ')).strip()
    p = float(input('digite o valor do produto: R$'))
    while True:
        k = str(input('voce deseja continuar [S/N]: ')).strip().upper()[0]
        if k == 'S' or k == 'N':
            break
    b.append(n)
    pa.append(p)
    t += p
    if p > 1000:
        c += 1
    if len(b) == 1:
        m = p
    else:
        if p < m:
            m = p
    if k == 'N':
        break

while m != pa[r]:
    r += 1

print(f'o total gasto na compra foi de {t}')
print(f'o numero de produtos acima de R$1000 foi de {c}')
print(f'o produto mais barato foi de {b[r]}')

