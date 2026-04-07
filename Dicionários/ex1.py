'''
1) Mesclar Dicionários:
Escreva uma função que receba dois dicionários como entrada e retorne um terceiro dicionário que seja a fusão
dos dois.
'''

def dicionario_mesclado (dicionario1,dicionario2):
    dic3 = {}
    for chave in dicionario1:
        dic3[chave] = dicionario1[chave]
    
    for chave in dicionario2:
        dic3[chave] = dicionario2[chave]
        
    return dic3

dicionario1 = {"A": 1, "B": 2, "C": 3}       # Dar ao usuario a opção de input
dicionario2 = {"C": 4, "D": 5, "E": 6}

print(dicionario1)
print(dicionario2)
print(dicionario_mesclado(dicionario1,dicionario2))