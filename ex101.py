def voto(ano):
    idade = 2025 - ano
    if idade < 18:
        print(f'com {idade} anos: NÃO VOTA')
    elif idade >= 18 and idade < 65:
        print(f'com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade >= 65:
        print(f'com {idade} anos: VOTO OPCIONAL')


a = int(input('digite o ano de nascimento: '))
voto(a)