def aumentar(preço, porcentagem):
    p = preço + preço * (porcentagem / 100)
    return p

n = int(input('Digite um preço: '))
print(f'Aumentando 10% temos {aumentar(n, 10)}')
