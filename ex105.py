def notas(* num, sit=False):
    aluno = {}
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['media'] = sum(num) / len(num)
    if sit==True:
        if aluno['media'] >= 7:
            aluno['sit'] = 'BOA'
        else:
            aluno['sit'] = 'RUIM'
    return aluno

#main
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)