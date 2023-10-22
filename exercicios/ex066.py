count = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    count += 1
print(f'foram digitados {count} números.\n'
      f'a soma entre eles é igual a {s}')
