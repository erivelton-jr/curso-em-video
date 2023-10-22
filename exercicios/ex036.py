from time import sleep
from emoji import emojize


print('\033[1:34m=^'*20)
print('Bem vindo ao Jr Imóveis')
print('=^'*20)

sleep(1)

val = float(input('\033[35mQual é o valor do imovel? '))
s = float(input('Qual é sua renda mensal? '))
a = float(input('Em quantos anos você irá pagar o imovel? '))
por = (s * 30) / 100
par = val / (a * 12)

print('\033[36mANALISANDO...')
sleep(3)

if par <= por:
    print(f'\033[32mParabéns! Você está apto para comprar a casa e as parcelas sairá por {par:.2f}$')
else:
    print('\033[4:31mInfelizmente você não poderá fazer este emprestimo.', emojize(':frowning_face:', language='en'))
