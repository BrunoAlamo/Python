def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuario')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero real valido')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuario')
            return 0
        else:
            return n

num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')