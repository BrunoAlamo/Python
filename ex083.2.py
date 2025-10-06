e = str(input('digite sua expressao: '))
p = []
for s in e:
    if s == '(':
        p.append('(')
    elif s == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('sua expressao é válida')
else:
    print('sua expressao está errada')