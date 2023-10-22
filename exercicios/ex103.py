def ficha(jog='<desconhecido>', gols=0):
    print(f'O {jog} fez {gols} gols')


n = str(input('Nome: '))
g = int(input('Gols: '))
ficha(n, g)
