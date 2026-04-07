# uso do get
'''
dic_estoque_frutas = {'apples': 430, 'bananas':
312, 'oranges': 525, 'pears': 217}
ks = list(dic_estoque_frutas.keys()) # Cria uma lista com as chaves
ks.append('kiwi')
print("Lista de frutas:", ks)
for k in ks:
    print(k, ": ", dic_estoque_frutas.get(k, "Não tem"))
'''
# vizualização do que cada coisa faz 
'''
dic_frutas_preço = {'apples': 4.30, 'bananas': 3.90, 'oranges': 5.25,
'pears': 7.50}
print(list(dic_frutas_preço.keys()))
print(list(dic_frutas_preço.values()))
print(list(dic_frutas_preço.items()))
'''
# uso do del 
'''
dic_estoque_frutas = {'kiwis': 430, 'bananas': 312,
'laranjas': 525, 'peras': 217}
print(dic_estoque_frutas)
del dic_estoque_frutas['peras']
print(dic_estoque_frutas)
'''
# uso do in e not in 
'''
dic_estoque_frutas = {'apples': 430, 'bananas': 312,
'oranges': 525, 'pears': 217}
print('apples' in dic_estoque_frutas)
print('cherries' in dic_estoque_frutas)
if 'bananas' in dic_estoque_frutas:
    print("Quantidade de bananas: ",dic_estoque_frutas['bananas'])
else:
    print("Nós não temos bananas!")
'''
# são mutaveis
'''
dic_estoque_frutas = {'kiwis': 430, 'bananas': 312,
'laranjas': 525, 'peras': 217}
dic_estoque_frutas['peras'] = 0                                       # achei a chave e zerei o valor
dic_estoque_frutas['bananas'] = dic_estoque_frutas['bananas'] + 200       # achei  valor e adicionei mais 200
numItems = len(dic_estoque_frutas)                                        # print do len total de items
print(dic_estoque_frutas)
print(numItems)
'''
# atribuições
'''
d1 = {"Catarina":5}
d2 = d1
print(d2 is d1)
d1["Jonas"] = 20
print(d2)
#saída: {"Catarina": 5, "Jonas": 20} 
'''
# copy 
'''
d1 = {"Joao": 10, "Maria":20}
d2 = d1.copy()
d2["Pedro"] = 30
d1["Joao"] = 40
print(d1)
# saída: {"Joao": 40,"Maria": 20}
print(d2)
# saída: {"Pedro": 30,"Joao": 10,"Maria": 20}
'''
# em caso de listas
'''
d1 = {"Joao":[1,2], "Maria":[3,4]}
d2 = d1.copy()
d2["Pedro"]=[5,6]
d1["Joao"] += [3]
print(d1)
# saída: {"Joao":[1, 2, 3], "Maria":[3, 4]}
print(d2)
# saída{"Pedro":[5, 6],"Joao":[1, 2, 3],"Maria": [3, 4]} 
idades = {"Joao":10, "Maria":12}
idadesCriancas = idades
idades.clear()                                             # uso do clear
print(idades)
# saída: {}
print(idadesCriancas)
# saída: {}
'''
# O método clear() é diferente da atribuição de {}:
# Para entender os endereçamentos de memória:
'''
idades = {"Joao": 10, "Maria": 12}
print("id(idades):", id(idades))
idadesCriancas = idades
print("id(idadesCriancas):", id(idadesCriancas))
idades = {}
print("id(idades) após reatribuição:",
id(idades))
print("idades:", idades)
print("idadesCriancas:", idadesCriancas)
'''
# uso do update 
'''
x = {"a":1, "b":2, "c":3}
y = {"z":9, "b":7}
x.update(y)
print(x)
# saída: {"a":1, "c":3, "b":7, "z":9}
x.update(a=7,c="xxx",b = 90)                            #   BRUXARIA
print(x)
# saída: {"a":7, "c":"xxx", "b":7, "z":9} 
'''
# Uso do pop
'''
notas = {"Joao":[9.0,8.0], "Maria": [10.0]}
print(notas.pop("Joao","aluno não encontrado"))                # bruxaria 2
# saída: [9.0,8.0]
print(notas)
# saída: {"Maria":[10.0]}
'''
# popitem()
'''
notas = {"Joao":[9.0,8.0],"Maria":[10.0]}
print(notas)
# saída: {'Joao': [9.0, 8.0], 'Maria': [10.0]}
print(notas.popitem())
# saída: ("Maria":[10.0])                           # remove o ultimo
print(notas)
# saída: {"Joao":[9.0, 8.0]} 
'''
# iteração
'''
notas = {"Joao":[9.0,8.0], "Maria":[10.0]}
for nome in notas:
    media = sum(notas[nome])/len(notas[nome])
    print("A média de ", nome, " é: ", media)

'''
# uso do dict()
'''
produtos = dict([(10, 4.5), (20, 5.99)])
valorProd = produtos[10]
print(valorProd)
# saída: 4.5
valorProd = produtos[20]
print(valorProd)
# saída 5.99
'''
'''
produtos = dict(10=4.5,20=5.99)
SyntaxError: keyword can't be an
expression
'''
'''
# Nesse caso as chaves precisam ser strings, mas são escritas sem aspas:              
# dict() com sequencia de itens chave=valor
produtos = dict(prod10=4.5,prod20= 5.99)
valorProd = produtos["prod10"]
print(valorProd)
# saída: 4.5
'''
'''
# {}.fromkeys(lista,valor)
dic1={}.fromkeys([2,3])
print("dic1=",dic1)
# saída: {2: None, 3: None}
dic2=dict.fromkeys(["Joao","Maria"],20)
print("dic2=",dic2)
# saída: {"Joao": 20, "Maria": 20} 
'''
# matrizes
'''
# padão mat=[[0,0,0,1,0],[0,0,0,0,0],[0,2,0,0,0],[0,0,0,0,0],[0,0,0,3,0]]
mat = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
print(mat[(0, 3)])
# com get
mat = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
print(mat.get((0,3)))
print(mat.get((1, 3), 0))
'''