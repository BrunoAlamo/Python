m = [[], [], []]
a = 0
b = 0
c = 0
while a != 3:
    n = int(input(f'digite um valor para [0, {a}]: '))
    m[0].append(n)
    a += 1
while b != 3:
    n = int(input(f'digite um valor para [1, {b}]: '))
    m[1].append(n)
    b += 1
while c != 3:
    n = int(input(f'digite um valor para [2, {c}]: '))
    m[2].append(n)
    c += 1
for v in m[0]:
    print(f'[ {v} ]', end='')
print()
for v in m[1]:
    print(f'[ {v} ]', end='')
print()
for v in m[2]:
    print(f'[ {v} ]', end='')
print()
sp = 0
for v in m[0]:
    if v % 2 == 0:
        sp += v
for v in m[1]:
    if v % 2 == 0:
        sp += v
for v in m[2]:
    if v % 2 == 0:
        sp += v
print(f'a soma de todos os valores pares é de {sp}')
print(f'a soma dos valores da terceira coluna é de {m[0][2] + m[1][2] + m[2][2]}')
print(f'o maior valor da segunda linha foi de {max(m[1])}')