a = []
c = 0
medias = []
while True:
    n = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = n1 + n2 / 2
    medias.append(m)
    a.append([[n1, n2], n])
    while True:
        s = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if s == 'S' or s == 'N':
            break
    if s == 'N':
        break
    c += 1
print('         MÉDIAS:')
for c in range(0, len(medias)):
    print(f'{c}  {a[c][1]}       {medias[c]}')
p = 0
while p != 999:
    e = int(input('Quer mostrar as notas de qual aluno? (999 interrompe): '))
    print(f'As notas de {a[e][1]} são: {a[e][0]}')