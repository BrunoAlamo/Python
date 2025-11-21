i = int(input('digite sua idade: '))
if i <= 9:
    print('voce está na categoria MIRIM')
elif i <= 14:
    print('voce esta na categoria INFANTIL')
elif i <= 19:
    print('voce esta na categoria JUNIOR')
elif i <= 20:
    print('voce esta na categoria SENIOR')
else:
    print('voce esta na categoria MASTER')