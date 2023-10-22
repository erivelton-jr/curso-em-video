matriz0 = [[], [], []]
matriz1 = [[], [], []]
matriz2 = [[], [], []]
for x in range(0, 3):
   matriz0[x].append(int(input(f'matriz na posição [0, {x}]: ')))
for y in range(0, 3):
   matriz1[y].append(int(input(f'matriz na posição [1, {y}]: ')))
for z in range(0, 3):
   matriz2[z].append(int(input(f'Matriz na posição [2, {z}]: ')))
print(f' {matriz0}')
print(matriz1)
print(matriz2)
