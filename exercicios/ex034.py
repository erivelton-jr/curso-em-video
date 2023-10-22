s = float(input('Quanto você recebe por mês?: '))
s1 = 1.30 * s
cores = dict(preto='\033[30m', azul='\033[34m')
if s > 1250:
    print(f"Parabéns! Você ganhou um aumento de 10%. Você vai receber{cores['preto']} {s * 1.10:.2f} $")
else:
    print(f" Parabens! você ganhou um aumento de 15%. Você vai receber {cores['azul']}{s * 1.15:.2f} $")
