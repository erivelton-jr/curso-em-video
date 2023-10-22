n = []
max = min = 0
for x in range(0,5):
    val = int(input('Diga um valor: '))
    n.append(val)

for x in range(0, 5):
    for y in range(0, 5):
        if (n[x] < n[y]):
            ord = n[x]
            n[x] = n[y]
            n[y] = ord

print(n)