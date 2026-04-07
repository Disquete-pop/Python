# Alunos=[ ['João', 18], ['Isabela', 17], ['Daniel', 19] ]
# # notas dos alunos – código da disciplina, nome da prova e nota
# Notas = [
# [ ['MAT', 'P1', 5.8], ['ALG', 'P1', 7.4], ['WEB', 'P1', 8.9], ['ALG', 'P2', 9.6] ], # provas do João
# [ ['ALG', 'P1', 9.2], ['WEB', 'P1', 6.7], ['WEB', 'P2', 9.3] ], # provas da Isabela
# [ ['MAT', 'P1', 5.8], ['ALG', 'P1', 9.6], ['MAT', 'P2', 8.1], ['MAT', 'P3', 8.1] ] # provas do Daniel
#  ] # fecha a lista de notas 

# def media_aluno(x):
#     aluno = False
#     for i in Alunos:
#         if i[0] == x:
#             aluno = True
#     if aluno == True:
#         texto = ''
#         valor_ind = 0
#         ac_mat = 0
#         cont_mat = 0
#         ac_web = 0
#         cont_web = 0
#         ac_alg = 0
#         cont_alg = 0
#         media_alg = 0
#         media_mat = 0
#         media_web = 0
#         lista_resulado=[]
#         for i in range(len(Alunos)):
#             if Alunos[i][0] == x:
#                 valor_ind = i
#         for nota in Notas[valor_ind]:
#             if nota[0] == 'MAT':
#                 ac_mat += nota[2]
#                 cont_mat += 1
#                 media_mat = ac_mat / cont_mat
#             elif nota[0] == 'ALG':
#                 ac_alg += nota[2]
#                 cont_alg += 1
#                 media_alg = ac_alg / cont_alg
#             elif nota[0] == 'WEB':
#                 ac_web += nota[2]
#                 cont_web += 1
#                 media_web = ac_web / cont_web       
#             else:
#                 print('invalido')
#         if media_mat > 0:
#             lista_resulado.append(['MAT: ',media_mat])
#         if media_alg > 0:
#             lista_resulado.append(['ALG: ',media_alg])
#         if media_web > 0:
#             lista_resulado.append(['WEB: ',media_web])
#         texto = x + ('\n')
#         for valor in lista_resulado:
#             texto += valor[0] + str(valor[1]) + ('\n')
#         return(texto)
#     else:
#         return('Nome invalido')

# # # maior nota por aluno:
# lista_notas = []
# notas_mat = ['Mat ',[],0]
# notas_alg = ['ALG',[],0]
# notas_web = ['WEB',[],0]
# mat = 0
# web = 0
# alg = 0
# '''
# 0 = mat
# 1 = alg
# 2 = web
# '''
# for i in range(len(Notas)):
#     for prova in Notas[i]:
#         if prova[0] == 'MAT':
#             if prova[2] > mat:
#                 notas_mat[1] = [Alunos[i][0]]
#                 notas_mat[2] = prova[2]
#                 mat = prova[2]
#             elif prova[2] == mat:
#                 if Alunos[i][0] not in notas_mat[1]:
#                     notas_mat[1].append(Alunos[i][0])
#         elif prova[0] == 'ALG':
#             if prova[2] > alg:
#                 notas_alg[1] = [Alunos[i][0]]
#                 notas_alg[2] = prova[2]
#                 alg = prova[2]
#             elif prova[2] == alg:
#                 if Alunos[i][0] not in notas_alg[1]:
#                     notas_alg[1].append(Alunos[i][0])
#         elif prova[0] == 'WEB':
#             if prova[2] > web:
#                 notas_web[1] = [Alunos[i][0]]
#                 notas_web[2] = prova[2]
#                 web = prova[2]       
#             elif prova[2] == web:
#                 if Alunos[i][0] not in notas_web[1]:
#                     notas_web[1].append(Alunos[i][0])
# resultado = []
# resultado.append(notas_mat)
# resultado.append(notas_alg)
# resultado.append(notas_web)  
# for valor in resultado:
#     print(valor)


# # Nome = input('Nome do aluno: ')
# # print(media_aluno(Nome))
# '''
# fita = [-1] * 10
# for i in range(len(fita)):
#     fita[i] = int(input('Para colorir a fita digite 0, para não -1'))
# for valor in fita:
    
# '''
# '''
# def delet(a,b):
#     if len(a) == 0:
#         return '', False
#     resto , removido = delet(a[1:],b)
#     if a[0] == b and not removido:
#         return resto, True
#     else:
#         return a[0] + resto, removido

# y = 'r'
# x = delet('arara',y)
# print(x)
# '''
# # print('iniciou')
# # def Matriz(a,b):
# #     mat = []
# #     for i in range(a):
# #         linha_atual = []
# #         for j in range(b):
# #             x = int(input(f'Valor de {[i]}{[j]}: '))
# #             linha_atual.append(x)
# #         mat.append(linha_atual)
# #     return mat

# # def SUB(A,B):
# #     sub = []
# #     for i in range(len(A)):
# #         linha_atual = []
# #         for j in range(len(A[0])):
# #             y = A[i][j] - B[i][j]
# #             linha_atual.append(y)
# #         sub.append(linha_atual)
# #     return(sub)


# # matA = Matriz(2,2)
# # print('Matriz A')
# # for valor in matA:
# #     print(valor)

# # matB = Matriz(2,2)
# # print('Matriz B')
# # for valor in matB:
# #     print(valor)

# # Res = SUB(matA,matB)
# # print('Resultado')
# # for valor in Res:
# #     print(valor)

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

# def prod(A,B):
#     mat = []
#     for i in range(AL):
#         Linha_atual = []
#         for k in range(BC):
#             soma = 0
#             for j in range(ACBL):
#                 soma += A[i][j] * B[j][k]
#             Linha_atual.append(soma)
#         mat.append(Linha_atual)
#     return(mat)

# AL = int(input('Linhas de A: '))
# BC = int(input('Colunas de B: '))
# ACBL = int(input('Valor de colunas de A e Linhas de B: '))
# MatA = Matriz(AL,ACBL)
# print('Matriz A')
# for valor in MatA:
#     print(valor)

# MatB = Matriz(ACBL,BC)
# print('Matriz B')
# for valor in MatB:
#     print(valor)

# produto = prod(MatA,MatB)
# print('Matriz produto')
# for valor in produto:
#     print(valor)

# def remove_ultima(p, y):
#     if p == "":
#         return "", False 

#     resto, removido = remove_ultima(p[1:], y)

#     if p[0] == y and not removido:
#         return resto, True  
#     else:
#         return p[0] + resto, removido
# p = 'Arara'
# y = 'r'
# resultado = remove_ultima(p, y)
# print(resultado)


# def fac(n,m):
#     if n < m:
#         return n
#     else:
#         return fac(n-m,m)
# x = 30
# y = 5
# print(fac(x,y))

# def a(n,m):
#     if len(n) == 0:
#         return m
#     else:
#        print(n[0])
#        return  a(n[1:],m + 1)

# m = 0
# n = 'Coiso'
# print(a(n,m))


# def Aa(x):
#     if len(x) == 0:
#         return
#     else:
#         print(x[0])
#         Aa(x[1:])
# def a(y):
#     l = []
#     for valir in range(y):
#         valor = int(input('Valor de {valir} da lista: '))
#         l.append(valir)
#     return(l)

# lista = a(10)
# print(lista)
# prin = Aa(lista)