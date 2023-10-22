aluno = {}
turma = []
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Média: '))

if aluno['Media'] >= 5:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k}: {v}')