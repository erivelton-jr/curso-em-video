c = {'roxo': '\033[30:45m',
     'branco': '\033[:7m',
     'vermelho': '\033[31m',
     'azul': '\033[:44m',
     'padrão': '\033[m'
     }

def ajuda():
    from time import sleep

    while True:

        print(c['roxo'], '-' * 30)
        print('Sistema de ajuda Python')
        print('-' * 30)
        x = input(f"{c['padrão']}Função ou biblioteca > ").strip().lower()

        if x == "fim":
            print(c['vermelho'], 'PROGRAMA FINALIZADO')
            break
        else:
            print(c['azul'], '~~' * 15)
            print(f'Acessando manual do {x}')
            print('~~' * 15)
            sleep(1)
            print(c['branco'])
            help(x)
            print(c['padrão'])


ajuda()

