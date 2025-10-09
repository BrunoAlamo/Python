a = {}

a['nome'] = str(input('digite o nome do aluno: '))
a['media'] = float(input('digite a media do aluno: '))

if a['media'] >= 7:
    a['situacao'] = 'APROVADO'
else:
    a['situacao'] = 'REPROVADO'

print(f'o nome é igual a {a["nome"]}')
print(f'a média é igual a {a["media"]}')
print(f'situação igual a {a["situacao"]}')