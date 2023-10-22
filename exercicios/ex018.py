import math
num = float(input('Digite um angulo: '))
x = math.radians(num)
sen = math.sin(x)
cos = math.cos(x)
tan = math.tan(x)
print(f'O ângulo de {num}° tem o SENO de {sen:.2f} \n'
      f'O ângulo de {num}° tem o COSSENO de {cos:.2f} \n'
      f'O ângulo de {num}° tem o de TANGENTE de {tan:.2f}.')
