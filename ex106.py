def ajuda(com):
    help(com)

def titulo(msg, cor):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)


#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp')
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    titulo('ATÉ LOGO!')
