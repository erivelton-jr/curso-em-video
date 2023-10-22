def resumo(n, a=0, d=0):
    print('-' * 40)
    print(f'RESUMO DOS FALORES')
    print('-' * 40)
    dobro = n * 2
    metade = n / 2
    aum = n + ((n * a) / 100)
    des = n - ((n * d) / 100)
    print(f'Preço analisado: R${n:.2f}')
    print(f'Dobro do preço: R${dobro:.2f}')
    print(f'Metade do preço: R${metade:.2f}')
    print(f'Com {d}% de desconto: R${des:.2f}')
    print(f'Com {a}% de acrescimo: R${aum:.2f}')


