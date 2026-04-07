'''
2) Calculadora de Média:
Escreva um programa que recebe um dicionário onde as chaves são nomes de alunos e os valores são listas de
notas. Calcule a média de cada aluno e retorne um novo dicionário com os nomes dos alunos e suas respecƟvas
médias.
'''

def calcula_media(dicio):
    dic2 = {}
    for chave in dicio:
        valor = dicio[chave]
        total = 0
        for lista in valor:
            total += lista
        total = (f'{total/len(valor):.4}')
        dic2[chave] = float(total)
    return dic2 

notas= {"Aluno1": [90, 85, 88],
        "Aluno2": [78, 92, 87],
        "Aluno3": [85, 90, 79]
        }
print(notas)
print(calcula_media(notas))