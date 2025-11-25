l = []

for c in range(0, 5):
    l.append(int(input(f'Digite um valor na posição {c}: ')))

print(f'o maior valor foi {max(l)} na posição ', end='')
for i, v in enumerate(l):
    if v == max(l):
        print(f'{i}...', end='')
print()
print(f'o menor valor foi {min(l)} na posição ', end='')
for i, v in enumerate(l):
    if v == min(l):
        print(f'{i}...', end='')
