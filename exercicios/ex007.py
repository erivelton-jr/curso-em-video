nome = input('Nome do aluno:')
n1 = float(input('Matemática - Prova I:'))
n2 = float(input('Matemática - Prova II: '))
s = (n1+n2)/2

print(f'{nome:=^40}\n'
      f'Prova I: {n1}\n'
      f'Prova 2: {n2}\n'
      f'Media: {s}')