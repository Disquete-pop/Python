# # ex 1
# Mat = []
# soma = 0
# soma2 = 0
# soma_linha = []
# for i in range(3):
#     soma = 0
#     linha_atual = []
#     for j in range(3):
        
#         x = int(input(f'Valor de {[i]}{[j]}: '))
#         linha_atual.append(x)
#         soma += x
#         soma2 += x
#     soma_linha.append([soma])
#     Mat.append(linha_atual)

# for v in Mat:/ 
#     print(v)
# print(soma_linha)
# print(soma2)

# # ex 2
# m = int(input('Valor de linhas: '))
# n = int(input('Valor de colunas: '))
# mat = []
# for i in range(m):
#     linha_atual = []
#     for j in range(n):
#         x = int(input(f'Valor de {[i]}{[j]}: '))
#         linha_atual.append(x)
#     mat.append(linha_atual)
# for valor in mat:
#     print(valor)

# # ex 3
# m = int(input('Valor de linhas: '))
# n = int(input('Valor de colunas: '))
# mat = []
# ac = 0
# for i in range(m):
#     linha_atual = []
#     for j in range(n):
#         x = int(input(f'Valor de {[i]}{[j]}: '))
#         linha_atual.append(x)
#     mat.append(linha_atual)
# print('Matriz 1')
# for valor in mat:
#     print(valor)


# for z in range(m):
#     for y in range(n):
#         if mat[z][y] == mat[z][z]:
#             print('',end='')
#             ac += mat[z][y]
#         else:
#             mat[z][y] = 0
# print('Matriz Diagonal')
# for valor1 in mat:
#     print(valor1)
# print(f'Valor acumulado {ac}')

# # ex 4
# m = int(input('Valor De linhas e colunas da matriz quadrada: '))
# mat = []
# for i in range(m):
#     linha_atual = []
#     for j in range(m):
#         if j == i:
#             x = 1
#             linha_atual.append(x)
#         else:
#             x = 0
#             linha_atual.append(x)
#     mat.append(linha_atual)
# for valor in mat:
#     print(valor)

# # ex 5
# m = int(input('Valor de linhas: '))
# n = int(input('Valor de Colunas: '))
# mat = []
# mat2 = []
# resultante = []
# print('Matriz 1')
# for i in range(m):
#     linha_atual = []
#     for j in range(m):
#         x = int(input(f'Valor de {[i]}{[j]}'))
#         linha_atual.append(x)
#     mat.append(linha_atual)
# for valor in mat:
#     print(valor)

# print('Matriz 2')
# for u in range(m):
#     linha_atual = []
#     for y in range(n):
#         e = int(input(f'Valor de {[u]}{[y]}'))
#         linha_atual.append(e)
#     mat2.append(linha_atual)
# for valo1r in mat2:
#     print(valo1r)
# print('Resultante:')
# for t in range(m):
#     linha_atual = []
#     for r in range(n):
#         res = mat[t][r] + mat2[t][r]
#         linha_atual.append(res)
#     resultante.append(linha_atual)
# for valo in resultante:
#     print(valo)

# # ex 6
# m = int(input('Valor de linhas: '))
# n = int(input('Valor de Colunas: '))
# mat = []
# mat2 = []
# print('Matriz 1')
# for i in range(m):
#     linha_atual = []
#     for j in range(n):
#         x = int(input(f'Valor de {[i]}{[j]}'))
#         linha_atual.append(x)
#     mat.append(linha_atual)
# for valor in mat:
#     print(valor)
# print('Transposta')
# for i in range(n):
#     linha_atual = []
#     for j in range(m):
#         y = mat[j][i]
#         linha_atual.append(y)
#     mat2.append(linha_atual)
# for valor2 in mat2:
#     print(valor2)

# # ex 7
# m = int(input('Valor de linhas e coluna: '))
# mat = []
# mat2 = []
# res = True
# for i in range(m):
#     linha_atual = []
#     for     j in range(m):
#         x = int(input(f'Valor {[i]}{[j]} '))
#         linha_atual.append(x)
#     mat.append(linha_atual)
# print('Matriz 1')
# for valor in mat:
#     print(valor)
# for k in range(m):
#     linha_atual2 = []
#     for l in range(m):
#         y = mat[l][k]
#         linha_atual2.append(y)
#     mat2.append(linha_atual2)
# print('Matriz transposta')
# for valor2 in mat2:
#     print(valor2)
# for q in range(m):
#     for w in range(m):
#         if mat[q][w] != mat2[q][w]:
#             res = False

# if res == False:
#     print('Não simetrica')
# else:
#     print('Simetrica')

# # ex 8
# m = int(input('Numero de linhas: '))
# n = int(input('Numero de colunas: '))
# mat = []
# mat_2 = []
# resultante = []
# for i in range(m):
#     linha_atual = []
#     for j in range(n):
#         x = int(input(f'Valor {[i]}{[j]} da matriz 1: '))
#         linha_atual.append(x)
#     mat.append(linha_atual)
# print('matriz 1')
# for val in mat:
#     print(val)
# for k in range(m):
#     linha_atual2 = []
#     for l in range(n):
#         y = int(input(f'Valor de {[k]}{[l]} da matriz 2: '))
#         linha_atual2.append(y)
#     mat_2.append(linha_atual2)
# print('Matriz 2')
# for v in range(m):
#     linha_atual3 = []
#     for w in range(n):
#         res = mat[v][w] - mat_2[v][w]
#         linha_atual3.append(res)
#     resultante.append(linha_atual3)
# print('Matriz resultante')
# for res in resultante:
#     print(res)

# ex 9
# m = 2 # linhas da primeria
# o = 4 # colunas da segunda
# n = 3 #  colunas da primeira e linhas da segunda

# mat = [[1,2,3]
#        ,[4,5,6]]
# mat2 =[[1,4,7,0],
#        [2,5,8,1],
#        [3,6,9,2],
#        ]
# resultante = []
# for i in range(m):
#     linha_atual=[]
#     for k in range(o):
#         soma = 0
#         for j in range(n):
#             soma = soma + mat[i][j] * mat2[j][k]  # linhas da primeira * coluna da segunda
#         linha_atual.append(soma)
#     resultante.append(linha_atual)
# for valor in resultante:
#     print(valor)

# #  eu fazendo

# a = int(input('Linha da primeira: '))
# b = int(input('Coluna da segunda: '))
# c = int(input('Linha da segunda e coluna da primeria: '))
# mat = []
# mat2 = []
# resultante = []
# for d in range(a):
#     linha_atual = []
#     for e in range(c):
#         x = int(input(f'Valor de {[a]}{[b]} mastriz 1'))
#         linha_atual.append(x)
#     mat.append(linha_atual)
# print('matriz 1')
# for valor in mat:
#     print(valor)
# # matriz 2
# for f in range(c):
#     linha_atual2 = []
#     for g in range(b):
#         y = int(input(f'Valor de {[c]}{[b]} da matriz 2'))
#         linha_atual2.append(y)
#     mat2.append(linha_atual2)
# print('Matriz 2 ')
# for valor2 in mat2:
#     print(valor2)
# #   produto
# for i in range(a):
#     linha_atual3 = []
#     for k in range(b):
#         soma = 0
#         for j in range(c):
#             soma += mat[i][j]*mat2[j][k]
#         linha_atual3.append(soma)
#     resultante.append(linha_atual3)
# print('Resultante')
# for valor3 in resultante:
#     print(valor3)

# # ex 10
mat = []
mat2 =[]
prod = []
a = 2
for i in range(a):
    linha_atual = []
    for j in range(a):
        x = int(input(f'Valor de {[i]}{[j]}: '))
        linha_atual.append(x)
    mat.append(linha_atual)
for k in range(a):
    linha_atual2 = []
    for l in range(a):
        y = int(input(f'Valor de {[k]}{[l]}: '))
        linha_atual2.append(y)
    mat2.append(linha_atual2)

for i in range(a):
    linha_atual3 = []
    for j in range(a):
        soma = 0
        for r in range(a):
           soma += mat[i][r] * mat2[r][j]
        linha_atual3.append(soma)
    prod.append(linha_atual3)
print('resultado')
for valor in prod:
    print(valor)
identidade = []
print('identidade')
for i in range(a):
    linha_atual4 = []
    for j in range(a):
        if i == j:
            linha_atual4.append(1)
        else:
            linha_atual4.append(0)
    identidade.append(linha_atual4)
for valor5 in identidade:
    print(valor5)
iguais = True
for i in range(a):
    for j in range(a):
        if prod[i][j] != identidade[i][j]:
            iguais = False

if iguais == True:
    print('é')
else:
    print('num é')
# print('iniciou')
# def Matriz(a,b):
#     mat = []
#     for i in range(a):
#         linha_atual = []
#         for j in range(b):
#             x = int(input(f'Valor de {[i]}{[j]}: '))
#             linha_atual.append(x)
#         mat.append(linha_atual)
#     return mat

# def SUB(A,B):
#     sub = []
#     for i in range(2):
#         linha_atual = []
#         for j in range(2):
#             y = A[i][j] - B[i][j]
#             linha_atual.append(y)
#         sub.append(linha_atual)
#     return(sub)


# matA = Matriz(2,2)
# print(matA)
# for valor in matA:
#     print(valor)
# matB = Matriz(2,2)
# for valor in matB:
#     print(valor)
#     def SUB(A,B):
'''
Resultado = SUB(matA,matB)
for valor in Resultado:
    print(valor)'''