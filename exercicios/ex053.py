f = str(input('Diga uma frase: ')).lower().strip().split()
x = ''.join(f)
r = ''

for c in range(len(x)-1, -1, -1):
    r += x[c]

print(f'A frase em reverso é {r}')

if r == x:
        print('é um palimedro')
else:
        print('não é um palimedro')