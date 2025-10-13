def area(a, b):
    field = a * b
    print(f'a area do seu terreno {a}x{b} é de {field}m^2')


print('CONTROLE DE TERRENOS')
print('-=' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)