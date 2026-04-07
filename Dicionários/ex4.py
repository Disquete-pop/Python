'''
4) União de Listas em Dicionário:
Crie uma função que receba duas listas, uma de chaves e outra de valores, e retorne um dicionário onde as chaves
e os valores são emparelhados.

'''
def união(lista_chaves,lista_valores = [1, 2, 3]):
    Veracidade = False
    dic = {}
    if len(lista_chaves) == len(lista_valores):
        for i in range(len(lista_chaves)):
            dic[lista_chaves[i]] = lista_valores[i]
        return dic
    else:
        return 'Os indices são diferentes!'

lista1 = ["A", "B", "C"]
lista2 = [1, 2, 3]

print(união(lista1,lista2))