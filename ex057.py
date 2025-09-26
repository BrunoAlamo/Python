s = 'M'

while s == 'M' or s == 'F':
    s = str(input('digite seu sexo: [M/F] ')).upper()
    if s != 'M' and s != 'F':
        print('digite apenas M ou F')