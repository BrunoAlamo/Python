def notas(* num):
    aluno = {}
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['media'] = sum(num) / len(num)
    return aluno

#main
resp = notas(5.5, 9.5, 10, 6.5)
print(resp)