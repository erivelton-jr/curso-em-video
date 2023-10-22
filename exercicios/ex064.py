n = cont = soma = 0
n = int(input('Digite um valor: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um valor: '))
print(f'a soma entre os {cont} valores é {soma}')
