def LeiaInt(msg):
    n = input(msg)
    x = 0

    if n.isnumeric():
        return int(n)
    else:
        return f'\033[31mvalor invalido'


n = LeiaInt('Digite um numero: ')
print(f'Você digitou {n}')