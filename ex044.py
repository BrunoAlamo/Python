p = float(input('digite o valor do produto: '))
f = input('digite 1 para a vista no dinheiro/cheque, 2 para a vista no cartao, 3 para 2x no cartao, 4 para 3x ou mais no cartao: ')

if f == '1':
    vf = p - p * 0.10
    print('o valor a ser pago será de: R${}'.format(vf))
elif f == '2':
    vf = p - p * 0.05
    print('o valor a ser pago será de: R${}'.format(vf))
elif f == '3':
    vf = p / 2
    print('o valor a ser pago por mês será de R${}'.format(vf))
elif f == '4':
    parcelas = int(input('digite a quantidade de parcelas: '))
    vf = (p + p * 0.20) / parcelas
    print('o valor a ser pago por mês será de R${}'.format(vf))