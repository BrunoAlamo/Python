m = 0

for c in range (1, 8):
    i = int(input('digite a sua idade: '))
    if i < 21:
        m += 1
print('{} pessoas ainda não são maiores de idade'.format(m))
print('{} pessoas são maiores de idade'.format(7-m))