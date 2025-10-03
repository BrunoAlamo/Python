f = input('digite uma expressao: ')

l = list(f)


e = l.count('(')
d = l.count(')')

print(e)
print(d)
while True:
    if d != 0 and e != 0:
        if f.index(')') < f.index('('):
            print('Sua expressão é inválida')
            break
        elif (e + d) % 2 == 0 and e == d:
            print('Sua expressão é válida')
            break
        else:
            print('Sua expressão é inválida')
            break
    elif d == 0 and e != 0:
        print('Sua expressão é inválida')
        break
    elif e == 0 and d != 0:
        print('Sua expressão é inválida')
        break
