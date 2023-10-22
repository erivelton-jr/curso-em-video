from ex108 import moedas

num = float(input('Diga um valor: '))
print(f'O dobro de {moedas.moeda(num)} é {moedas.moeda(moedas.dobro(num))}')
print(f'A metade de {moedas.moeda(num)} é {moedas.moeda(moedas.metade(num))}')
print(f'{moedas.moeda(num)} com aumento de 10% fica {moedas.moeda(moedas.aumentar(num, 10))}')
print(f'{moedas.moeda(num)} com desconto de 30% fica {moedas.moeda(moedas.diminuir(num, 30))}')