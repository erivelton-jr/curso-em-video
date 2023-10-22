from ex109 import moedas

num = float(input('Diga um valor: '))
print(f'O dobro de {moedas.moeda(num)} é {moedas.dobro(num, False)}')
print(f'A metade de {moedas.moeda(num)} é {moedas.metade(num, True)}')
print(f'{moedas.moeda(num)} com aumento de 10% fica {moedas.aumentar(num, 10, True)}')
print(f'{moedas.moeda(num)} com desconto de 30% fica {moedas.diminuir(num, 50, True)}')