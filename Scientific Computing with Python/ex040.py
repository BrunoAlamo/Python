n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('voce foi reprovado')
elif media >= 5 and media <7:
    print('voce esta de recuperacao')
elif media >=7:
    print('voce foi aprovado')