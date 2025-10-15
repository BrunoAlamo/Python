def fatorial(n, show=False):
    c = 1
    f = 0
    print(f'{n}', end='')
    while c != n:
        print(f' x {n - c}', end='')
        f += n * (n - c)
        c += 1
    print(' = ', end='')
    print(f)



fatorial(5)