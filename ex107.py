import moeda

n = int(input('Digite um preço: '))
print(f'Aumentando 10% temos {moeda.aumentar(n, 10)}')
print(f'A metade do {n} é {moeda.metade(n)}')
print(f'O dobro de {n} é {moeda.dobro(n)}')
print(f'Reduzindo 13%, temos {moeda.reduzir(n, 13)}')