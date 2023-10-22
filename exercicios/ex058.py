from random import randint
from time import sleep

print('=' * 70)
print('\033[32mESTOU PENSANDO EM UM NUMERO ENTRE 0 E 10. TENTE ADVINHAR...\033[m')
print('=' * 70)

sleep(1)

n = 12
cont = 0
while n != randint(0, 10):
    n = int(input('Qual numero estou pensando? '))
    cont += 1
print(f'\033[33mAcertou mizeravi!\n'
      f'\033[31mFoi necessaria {cont} tentativas para acertar')
