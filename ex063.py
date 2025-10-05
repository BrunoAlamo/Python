n = int(input('quantos termos da sequencia de Fibonacci voce quer mostrar? '))

t1 = 0
t2 = 1
t3 = 1
f = [t1, t2, t3]
r = 0

for c in range(1, n - 2):
    f.append(f[c] + f[c + 1])

while n != 0:
    print(f[r], end=' ')
    r += 1
    n -= 1



