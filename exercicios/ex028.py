from time import sleep
import random
print("~~" * 30)
print("Estou pensando em um numero entre 0 e 5, tente advinhar...")
print("~~" * 30)
n1 = int(input('Qual numero estou pensando? '))
print('PROCESSANDO...')
sleep(3)
if n1 == random.randint(0, 5):
    print('Acertou, Mizeravi!')
else:
    print('ERROOU!')
