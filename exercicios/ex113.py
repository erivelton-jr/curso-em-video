while True:
    try:
        n = int(input('Digite um numero inteiro: '))
    except ValueError:
        print('\033[31mErro! Você digitou um valor invalido.\033[m')
    else:
        break
while True:
    try:
        n2 = float(input('Digite um numero real: '))
    except ValueError:
        print('\033[31mErro! Você digitou um valor invalido.\033[m')
    else:
        break
print(f'Numero inteiro: {n}\nNumero real: {n2}')
