def leiadinheiro(x):
    valido = False
    while not valido:
        entrada = str(input(x)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '' or entrada.isalnum():
            print('\033[31mErro! Valor invalido.\033[m')
        else:
            valido = True
            return float(entrada)
