x = int(input('Você quer a tabuada de qual numero? '))

print('-' * 15)
for y in range(0, 10, 1):
    print(f'\033[35m{x} x {y} = {x * y}')
print('\033[m-' * 15)