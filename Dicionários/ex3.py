'''
3) Maior Valor por Chave:
Escreva uma função que receba um dicionário onde as chaves são strings e os valores são números. A função deve
retornar a chave associada ao maior valor no dicionário.
'''

def chave_maior(dicionario_notas):
    f = False
    for chave in dicionario_notas:
        if f == False:
            maior = dicionario_notas[chave]
            chave_ = chave
            f = True
        if dicionario_notas[chave] > maior:
            maior = dicionario_notas[chave]
            chave_ = chave
    return (f'{chave_} = {dicionario_notas[chave_]}')


dicionario_notas = {
                    "Aluno_1": 90,
                    "Aluno_2": 78,
                    "Aluno_3": 85,
                    "Aluno_4": 92
                    }

print(chave_maior(dicionario_notas))