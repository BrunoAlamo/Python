p = {}

while True:
    p['nome'] = str(input('Nome: '))
    a = int(input('ano de nascimento: '))
    i = 2025 - a
    p['idade'] = i
    p['ctps'] = int(input('Carteira de trabalho (0 para parar): '))
    if p['ctps'] == 0:
        break
    else:
        c = int(input('Ano de contratação: '))
        p['contratação'] = c
        p['salário'] = int(input('Salário: R$'))
        break
print(p)
if p['ctps'] != 0:
    for k, v in p.items():
        print(f'{k} tem o valor {v}')
    aposentadoria = c - a + 35
    print(f'aposentadoria tem o valor {aposentadoria}')
if p['ctps'] == 0:
    for k, v in p.items():
        print(f'{k} tem o valor {v}')