'''
5) Filtrar Dicionário:
Crie uma função que receba um dicionário (a chave é um número inteiro, e o valor é uma lista de strings), e uma
lista com algumas chaves. A função deve retornar um novo dicionário contendo apenas as chaves fornecidas na
lista
'''
def Filtra(dicio,lista):
    dic = {}
    for chave in dicio:
        if chave in lista:
            dic[chave] = dicio[chave]
    return dic

dicio = { 1:['A'] , 2:['B','C'], 3:['D','E','F'], 4:[], 5:['G'] }
lista = [2,4,5]

print(dicio)
print(lista)
print(Filtra(dicio,lista))