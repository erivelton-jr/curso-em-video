n = int(input('Qual é a distancia até o local da viagem? '))
x = n * 0.50
y = n * 0.45
if n <= 200:
    print(f'a Viagem irá custar: {x} $')
else:
    print(f'A viagem irá custar: {y} $')