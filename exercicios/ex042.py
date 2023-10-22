a = float(input('Valor da primeira reta: '))
b = float(input('Valor da segunda reta: '))
c = float(input('Valor da terceira reta: '))
retas = sorted([a, b, c], reverse=True)
soma = retas[1] + retas[2]

if soma < retas[0]:
    print("Com esses valores é possivel criar um triangulo")
    if a != b != c != r1:
        print("É possivel formar um triangulo é escaleno.")
    elif retas[1] == retas[2]:\
        print("É possivel formar um triangulo isoceles.")
else:
    print("É possivel formar um triangulo equilatero.")