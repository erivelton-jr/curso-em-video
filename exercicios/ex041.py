from datetime import date

n = int(input('Ano de nascimento: '))
i = date.today().year - n

if i <= 9:
    print(f'Você tem {i} anos, irá participar da classe MIRIM.')
elif i <= 14:
    print(f'Você tem {i} anos, irá participar da classe INFANTIL.')
elif i <= 19:
    print(f'Você tem {i} anos, irá participar da classe JUNIOR.')
elif i <= 25:
    print(f'Você tem {i} anos, irá participar da classe SÊNIOR.')
else:
    print(f'Você tem {i} anos, irá participar da classe MASTER.')
