p = {}
g = []
w = []
velhos = {}
vl = []
m = 0
o = 0
q = 1
while True:
    n = str(input('Nome: '))
    while True:
        s = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if s == 'M' or s == 'F':
            break
    i = int(input('Idade: '))
    while True:
        c = str(input('Que continuar? [S/N]: ')).strip().upper()[0]
        if c == 'S' or c == 'N':
            break
    o += i
    m = o / q
    q += 1
    p['nome'] = n
    p['sexo'] = s
    p['idade'] = i
    g.append(p)
    if s == 'F':
        w.append(n)
    p = {}
    if i > m:
        velhos['nome'] = n
        velhos['sexo'] = s
        velhos['idade'] = i
        vl.append(velhos)
    velhos = {}
    if c == 'N':
        break
print('-=' * 30)
print(f'O número de pessoas cadastradas foi de {len(g)}')
print(f'A media de idade do grupo é de {m} anos')
print('As mulheres cadastradas foram: ', end='')
for t in w:
    print(f'{t} ', end=' ')
print()
print('A lista de pessoas com idade acima da média foi: ')
for h in range(0, len(vl)):
    for k, v in vl[h].items():
        print(f'{k} = {v}; ', end='')