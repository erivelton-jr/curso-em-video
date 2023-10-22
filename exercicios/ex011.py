x = float(input('Altura da parede: '))
y = float(input('Largura da parede: '))
m2 = x*y
m = m2/2
print(f'sua parede tem a dimensão de{x}X{y}, ou seja, tem {m2}m². '
      f'Para pintar essa parede será necessário {m:.1f}l de tinta.')
