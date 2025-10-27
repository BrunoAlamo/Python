def aumentar(preço, porcentagem):
    p = preço + preço * (porcentagem / 100)
    return p

def dobro(preço):
    p = preço * 2
    return p

def metade(preço):
    p = preço / 2
    return p

def reduzir(preço, porcentagem):
    p = preço - preço * (porcentagem / 100)
    return p
