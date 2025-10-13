def maior(* num):
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v}', end=' ')
    print()
    print(f'o maior número digitado foi de {max(num)}')

maior(2, 3, 6, 33, 200, 133)
