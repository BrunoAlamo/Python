t = ('arroz', 'feijao', 'maionese', 'ketchup', 'josimar', 'jose', 'macio')
v = ('a', 'e', 'i', 'o', 'u')

vp = ''

h = 0
c = 0

while c != len(t):
    for d in range(0, len(v)):
        if v[d] in t[h]:
            vp += v[d]
            if t[h].count(v[d]) > 1:
                vp += v[d]
    print(f'{t[c]} tem as vogais: {vp}')
    vp = ''
    c += 1
    h += 1
