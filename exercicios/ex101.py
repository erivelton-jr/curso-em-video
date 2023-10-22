def voto(nasc):
    from datetime import date
    x = date.today().year - nasc
    if x < 16:
        return f'você tem {x} anos: Não vota'
    elif 18 >= x <= 65:
        return f'Você tem {x} anos: Voto obrigatorio'
    else:
        return f'Você tem {x} anos: Voto opcional'


i = int(input('Qual ano você nasceu: '))
print(voto(i))