n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

if n1 > 10 or n2 > 10:
    print('Erro! Reinicie o programa.')
elif m >= 7:
    print(f'\033[33mParabéns! sua média foi {m:.1f},Você está aprovado na matéria!')
elif m < 5:
    print(f'\033[31mSua media foi {m:.1f}, infelizmente você foi reprovado.')
else:
    print(f'\033[mSua media foi {m:.1f}. Você está de recuperação.')