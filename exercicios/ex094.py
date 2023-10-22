dados = {}
soma = 0
mulher = pessoa = []

while True:
    dados['Nome'] = input('Nome: ')
    while True:
        dados['Sexo'] = input('Sexo[M/F]: ').upper()
        if dados['Sexo'] in 'MF':
            break
        print('Erro. Deve ser [M/F]')
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    pessoa.append(dados.copy())
    while True:
        play = input('Deseja Continuar? [S/N] ').strip().upper()[0]
        if play in 'SN':
            break
        print('Erro. Deve ser [S/N]')
    if play == 'N':
        break
print('=' * 30)
print(f'Ao todo temos {len(pessoa)} pessoas.')
media = soma / len(pessoa)
print(f'A média de idade é {media:.2f} anos.')
print(f'As mulheres do grupo são: ', end='')
for m in pessoa:
    if m['Sexo'] == 'F':
        print(f"{m['Nome']} ")
print('Pessoas acima da media')
for x in pessoa:
    if x['Idade'] > media:
        print(f"{x['Nome']} = {x['Idade']}")