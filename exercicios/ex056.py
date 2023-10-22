f = 0
m = 0
idade = 0
homemvelho = 0
nomehomem = ''
mulhernova = 0
for p in range(1, 5):
    nome = str(input(f'Nome da {p}ª pessoa: ')).strip().title()
    id = int(input(f'Idade da {p}ª pessoa: '))
    idade += id
    s = str(input(f'Sexo da {p}ª pessoa (M/F): ')).strip().upper()
    print('-' * 50)

    if s == 'F':
        f += 1
        masc = 4 - f
    if p == 1 and s == 'M':
        homemvelho = id
        nomehomem = nome
    if s in 'M' and id > homemvelho:
        homemvelho = id
        nomehomem = nome
    if s in 'F' and id < 20:
        mulhernova += 1

m = idade / 4
print(f'A media de idade do grupo é de {m} anos\n')
print(f'no grupo tem {f} mulher(res) e {masc} homem(ens)')
print(f'O homem mais velho do grupo tem {homemvelho} anos e seu nome é {nomehomem}')
print(f'No grupo tem {mulhernova} mulher(res) com menos de 20 anos')