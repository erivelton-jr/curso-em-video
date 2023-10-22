from datetime import datetime

hj = datetime.today().year
cont = 0
for i in range(1, 8):
    id = int(input(f'ano em que a {i}ª pessoa nasceu: '))
    if hj - id < 17:
        cont += 1
        resto = 7 - cont

print(f'tem {cont} pessoas menor de idade\n'
      f'tem {resto} pessoas maior de idade')
