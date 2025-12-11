cv = int(input('digite a velociade do carro: '))
m = (cv-80)*7
if cv > 80:
    print('voce foi multado')
    print('o valor da multa será de R${:.2f}'.format(m))
else:
    print('voce nao foi multado')