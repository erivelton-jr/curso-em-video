x = int(input('digite um numero: '))

for c in range(1, x+1):
    if x % c == 0:
        print(f'\033[34m{c}', end=' ')
    else:
        print(f'\033[32m{c}', end=' ')
