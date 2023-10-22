from unidecode import unidecode
frase = str(input('Digitie uma frase: ')).strip().upper()
frase1 = unidecode(frase)
print(f'Quantas vezes aparece a letra A? {frase1.count("A")} \n'
      f'Em que posição ela aparece na primeira vez? {frase1.find("A") + 1} \n'
      f'Em que posição aparece na ultima vez? {frase1.rfind("A") + 1}')
