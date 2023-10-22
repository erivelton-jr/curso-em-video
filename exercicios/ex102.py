def fatorial(n=0, show=False):
    """
    ► Calcule Fatorial de um numero.
    :param n: Valor a ser calculado
    :param show: Mostrar ou não a solução
    :return: o resultado da fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            print(' = ' if c == 1 else ' x ', end='')
        f *= c
    return f


n = int(input('Fatorial de qual numero: '))
t = str(input('Quer ve a solução? '))
if t in 'Ss':
    show=True
elif t in 'Nn':
    show=False

print(fatorial(n, show))
