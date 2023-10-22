from random import randint

def sorteio():
    n = []
    p = []
    print(f'Os valores são: ', end='')
    for x in range(0, 5):
        n.append(randint(0, 10))
        print(f'{n[x]} ', end='')
        if n[x] % 2 == 0:
            p.append(n[x])
    print()
    somapar(sum(p))

def somapar(x):
    print(f'A soma entre os valores par são: {x}')


sorteio()
