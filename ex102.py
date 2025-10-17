from ctypes import c_char


def fatorial(n, show=False):
    c = n
    f = 1
    if show==True:
        print(f'{n}', end='')
        while c > 0:
            if c > 1:
                print(f' x {c - 1}', end='')
                f *= c
                c -= 1
            else:
                print(f' {c}', end='')
                break
        print(' = ', end='')
        print(f)
    else:
        while c > 0:
            f *= c
            c -= 1
        print(f)



fatorial(5)
fatorial(6, True)