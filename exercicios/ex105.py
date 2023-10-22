def notas(*n, sit=False):
    '''
    ► SISTEMA DE NOTAS:
    :param n: notas dos alunos
    :param sit: Mostrar ou não a situação da turma
    :return: dicionario com os dados da turma
    '''

    resp = dict()

    resp['TOTAL'] = len(n)
    resp['MAIOR'] = max(n)
    resp['MENOR'] = min(n)
    resp['MEDIA'] = sum(n) / resp['TOTAL']
    if sit is True:
        if resp['MEDIA'] < 5:
            resp['SIUAÇÃO'] = 'RUIM'
        elif resp['MEDIA'] > 7:
            resp['SIUAÇÃO'] = 'OTIMA'
        else:
            resp['SIUAÇÃO'] = 'RAZOAVEL'
    return resp


resp = notas(5, 2.5, 4.2, 7, sit=True)
print(resp)