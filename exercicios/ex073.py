times = ('Brasil', 'Suiça', 'Camarões', 'Servia')

print(f'Tabela: {times[0:]}')
print('-' * 50)
print(f'Os dois classificados são: {times[0:2]}')
print('-' * 50)
print(f'Os 2 ultimos colocados são: {times[-2:]}')
print('-' * 50)
print(f'Times em ordem alfabetica: {sorted(times[0:4])}')
print('-' * 50)
print(f'Brasil está na {times.index("Brasil")+1}ª posição.')
