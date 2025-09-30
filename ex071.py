import math

v = int(input('digite o valor que quer sacar: R$'))
n = [50, 20, 10, 5, 2, 1]

while True:
    if v % 50 == 0:
        print(f'Total de {v / 50} cédulas de R$50')
        break
    if (v % 50) % 20 == 0:
        print(f'Total de {math.floor(v / 50)} cédulas de R$50')
        print(f'Total de {math.floor((v % 50) / 20)} cédulas de R$20')
        break
    if ((v % 50) % 20) % 10 == 0:
        print(f'Total de {math.floor(v / 50)} cédulas de R$50')
        print(f'Total de {math.floor((v % 50) / 20)} cédulas de R$20')
        print(f'Total de {math.floor(((v % 50) % 20) / 10)} cédulas de R$10')
        break
    if (((v % 50) % 20) % 10) % 5 == 0:
        print(f'Total de {math.floor(v / 50)} cédulas de R$50')
        print(f'Total de {math.floor((v % 50) / 20)} cédulas de R$20')
        print(f'Total de {math.floor(((v % 50) % 20) / 10)} cédulas de R$10')
        print(f'Total de {math.floor((((v % 50) % 20) % 10) / 5)} cédulas de R$5')
        break
    if ((((v % 50) % 20) % 10) % 5) % 2 == 0:
        print(f'Total de {math.floor(v / 50)} cédulas de R$50')
        print(f'Total de {math.floor((v % 50) / 20)} cédulas de R$20')
        print(f'Total de {math.floor(((v % 50) % 20) / 10)} cédulas de R$10')
        print(f'Total de {math.floor((((v % 50) % 20) % 10) / 5)} cédulas de R$5')
        print(f'Total de {math.floor(((((v % 50) % 20) % 10) % 5) / 2)} cédulas de R$2')
        break
    if (((((v % 50) % 20) % 10) % 5) % 2) % 1 == 0:
        print(f'Total de {math.floor(v / 50)} cédulas de R$50')
        print(f'Total de {math.floor((v % 50) / 20)} cédulas de R$20')
        print(f'Total de {math.floor(((v % 50) % 20) / 10)} cédulas de R$10')
        print(f'Total de {math.floor((((v % 50) % 20) % 10) / 5)} cédulas de R$5')
        print(f'Total de {math.floor(((((v % 50) % 20) % 10) % 5) / 2)} cédulas de R$2')
        print(f'Total de {math.floor((((((v % 50) % 20) % 10) % 5) % 2) / 1)} cédulas de R$1')
        break