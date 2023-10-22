from exercicios.ex107 import moedas

num = float(input('Diga um valor: '))
print(f'O dobro de {num}$ é {moedas.dobro(num)}$')
print(f'A metade de {num}$ é {moedas.metade(num)}$')
print(f'{num}$ com aumento de 10% fica {moedas.aumentar(num, 10)}$')
print(f'{num}$ com desconto de 30% fica {moedas.diminuir(num, 30)}$')