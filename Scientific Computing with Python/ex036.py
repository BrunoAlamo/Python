casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos =  int(input('Quantos anos você pretende pagar? '))

p = casa / (anos * 12)

if p <= salario * 0.3:
    print('Você pode comprar a casa, sua prestação será de R${} por mês'.format(p))
else:
    print('Você não pode comprar a casa pois a prestação de {} excede mais de 30% do seu salário'.format(p))