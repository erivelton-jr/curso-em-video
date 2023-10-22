produtos = ('Banana', 2.50, 'Limão', 0.80, 'Cafe', 12)
print('-' * 40)
print('PRODUTOS')
print('-' * 40)

for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<30}', f'R$ {produtos[i+1]:.2f}')