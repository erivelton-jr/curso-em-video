from datetime import date

pessoa = {}
while True:
    pessoa['Nome'] = str(input('Nome: '))
    ano = int(input('Ano de nascimento: '))
    pessoa['Idade'] = date.today().year - ano
    pessoa['CTTPS'] = int(input('Carteira de Trabalho (0 se não tem): '))
    if pessoa['CTTPS'] != 0:
        pessoa['Contrato'] = int(input('Ano de contrato: '))
        pessoa['P. Emprego'] = pessoa['Contrato'] - ano
        pessoa['Salario'] = float(input('Salario: '))
        pessoa['Sexo'] = str(input('Sexo: ')).strip()
        if pessoa['Sexo'] in 'Mm':
            pessoa['Aposentadoria'] = 35 + pessoa['P. Emprego']
        elif pessoa['Sexo'] in 'Ff':
            pessoa['Aposentadoria'] = 30 + pessoa['P. Emprego']
        break
    else:
        break
for i, v in pessoa.items():
    print(f'- {i}: {v}')