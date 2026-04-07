# linguagem compilada e interpretada. 
# compilador: analisa e se tiver erro não vira um binario interpretado
# interpretador: pode ter erro mas pode ser executado (html)
# base gramatical
# listas são delimitadas por colchetes [separados,por,virgulas]
# Endereços, codigo agora começa a ter ''predios''
# o indice sempre começa em zero!!!
lista_dentro_da_outra = [0,1,2,3,4,[0,1,2,3]] #valores indexaveis
#posição 5 é a outra lista
#bobble e mergshort organizar itens
# string imutavel para poupar memoria, tem proposito.
A = [10,8,5,2,6]
'''print(A[10]) # IndexError: list index out of range'''
lista_vazia = []
# lista em python pode ser hetrerogenia, pode ter valores de carater diferentes, string, int, float.
lista = [0] * 10
print(lista)
lista2 = [0.0 for i in range(10)]
print(lista2)
lista3 = list()
print(lista3)
lista[1] = 10     #pode-se fazer contas por fora. i = i + 1... 
print(lista)

'''lista.append(valor) # adiciona no ultimo indice, cria um novo elemento'''
for valor in lista:
    print()
    break
    #repetição é igual



print(lista[1:3]) # fatiamento  indice negativo começa em -1



# apagar elemento
del lista[2] / lista.remove('''elemnto,valor...''')
# string é imutavel, lista não