exp = str(input('Digite a expressão: '))
par = []
for simb in exp:
    if simb == '(':
        par.append('(')
    elif simb == ')':
        if len(par) > 0:
            par.pop()
        else:
            par.append(')')
            break
if len(par) == 0:
    print('Expressão vállida')
else:
    print('Expressão invalida!')
