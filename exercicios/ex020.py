from random import sample, shuffle
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
#print(f'A ordem de apresentação do trabalho será: {sample(lista, k=4)}')#
print(f'A ordem de apresentação será{lista}')

