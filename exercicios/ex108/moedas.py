def moeda(n):
    return f'R${n}'

def metade(n):
    return f'R${n/2:.2f}'

def dobro(n):
    return f'{n * 2:.2f}'

def aumentar(n, y=0):
    return f'{((n * y) / 100) + n:.2f}'

def diminuir(n, y=0):
    return f'{n - ((n * y) / 100):.2f}'
