maior = menor = 0
pessoas = []
dados = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    con = str(input('Deseja continuar? ')).strip()
    if con in 'Nn':
        break

print(f'Você cadastrou {len(pessoas)} pessoas.\n'
      f'o maior peso da lista foi: {maior}kg\n'
      f'o menor peso foi: {menor}kgs')
for p in pessoas:
    if p[1] == maior:
        print(f)