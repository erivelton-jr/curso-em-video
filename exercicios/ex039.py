from datetime import date
a = int(input('Ano de nascimento: '))
s = str(input('Qual é o seu sexo(F/M) : ')).upper()
ali = date.today().year
idade = ali - a

if idade > 17 and s == 'M':
    print(f'Você já tem {idade} anos, Alistamento obrigatorio.')
elif idade > 17 and s == 'F':
    print(f'Você já tem {idade} anos, porém o alistamento não é obrigatorio.')
else:
    print('Você não pode se alistar ainda.')