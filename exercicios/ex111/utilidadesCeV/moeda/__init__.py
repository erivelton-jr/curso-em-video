def moeda(n):
    return f'R${n:.2f}'

def metade(n, rs=False):
    s = n/2
    if rs is True:
        return f'R${s:.2f}'
    else:
        return f'{s:.2f}'

def dobro(n, rs=False):
    s = n * 2
    if rs is True:
        return f'R${s:.2f}'
    else:
        return f'{s:.2f}'

def aumentar(n, y=0, rs=False):
    s = ((n * y) / 100) + n
    if rs is True:
        return f'R${s:.2f}'
    else:
        return f'{s:.2f}'

def diminuir(n, y=0, rs=False):
    s = n - ((n * y) / 100)
    if rs is True:
        return f'R${s:.2f}'
    else:
        return f'{s:.2f}'
