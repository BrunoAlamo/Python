def area(a, b):
    area = a * b
    print(f'a area do seu terreno {a}x{b} é de {area}m^2')


print('CONTROLE DE TERRENOS')
print('-=' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)