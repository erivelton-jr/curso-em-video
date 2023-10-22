nome = str(input('Diga seu nome completo: ')).strip()
letras = nome.split()
x = ''.join(letras)
y = letras[0]
print(f'Seu nome é: {nome.upper()}.')
print(f'O nome {nome.lower()} tem {len(x)} letras')
print(f"O Primeiro nome tem {len(y)} letras")


'''nome = str(input('Diga seu nome: ')).strip()
print(f'seu nome em maiusculo é: {nome.upper()}')
print(f'seu nome em minusculo é: {nome.lower()}')
print(f'seu nome tem {len(nome) - nome.count(" ")}')
print(f'seu primeiro nome tem {nome.find(" ")}')'''
