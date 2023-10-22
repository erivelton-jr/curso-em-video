from random import sample, choice
from time import sleep

jokepo = str(input('Escolha um: ')).upper().strip()

print(f'PEDRA, PAPEL TEEE...', end='')
sleep(1)
print('SOURA')



jogo = 'PEDRA PAPEL TESOURA'.split()
lista = choice(jogo)


if jokepo == 'PEDRA' and lista == 'TESOURA':
    print(f'Você escolheu {jokepo}, e eu {lista} você ganhou')
elif jokepo == 'PAPEL' and lista == 'PEDRA':
    print(f'Você escolheu {jokepo}, e eu {lista} você ganhou')
elif jokepo == 'TESOURA' and lista == 'PAPEL':
    print(f'Você escolheu {jokepo} e eu {lista} você ganhou.')
elif jokepo == lista:
    print(f'eu escolhi {lista} e você {jokepo}. Empate')
elif jokepo != jogo:
    print('Errado! Jogue novamente.')
else:
    print(f'Eu escolhi {lista} e você {jokepo}. Ganhei!!!')
