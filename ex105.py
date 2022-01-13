def notas(*n,sit=False):
    """
    -> FUNÇÃO PARA ANALISAR NOTAS E SITUAÇÕES DE ALUNOS.
    :param n:UMA OU MAIS NOTAS DE ALUNOS, ACEITA VÁRIAS.
    :param sit: VALOR OPCIONAL INDICANDO SE DEVE OU NÃO ADD A SITUAÇÃO DO ALUNO.
    :return:DICIONÁRIO COM VÁRIAS INFORMAÇOES SOBRE A SITUAÇÃO DA TURMA.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(10,8,5.5,8,10,sit=True)
print(resp)
#help(notas)

