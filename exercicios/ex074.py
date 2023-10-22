from random import sample
num = tuple(sample(range(0, 10), k=4))
print(f'Os numeros sorteados foram: {num}')
print(f'O menor valor é: {min(num)}')
print(f'O maior valor é: {max(num)}')
