# # ex 1
# Frase = 'Frase de exemplo'
# cont = 1
# for i in Frase:
#     cont+=1
# print(cont)

# # ex 2
# for i in Frase:
#     if i != ' ':
#         cont += 1
# print(cont)

# # ex 3
# x = input('O que buscas? ')
# a = False
# for i in Frase:
#     if i == x:
#         a = True
# print(a)

# # ex 4
# for i in Frase:
#     if i == ' ':
#         cont+=1
# print(cont)

# # ex 5
# x = input('Buscar a ultima ocorrencia: ')
# for i in range(len(Frase)):
#     if Frase[i] == x:
#         cont = i
# print(cont)

# # # ex 6
# x = input('Valor que buscas: ')
# flag = True
# ex = ''
# for i in range(len(Frase)):
#     if Frase[i] == x and flag == True:
#         flag = False
#     else:
#         ex += Frase[i]
# print(ex)

# # ex 7
# a = Frase[::-1]
# ex = ''
# x = input('Valor que buscas: ')
# flag = True
# for i in range(len(a)):
#     if a[i] == x and flag == True:
#         flag = False
#     else:
#         ex += a[i]
# A = ex[::-1]
# print(A)

# # ex 8
# x = input('Valor que buscas: ')
# ex = ''
# for i in range(len(Frase)):
#     if Frase[i] == x:
#         print(end='')
#     else:
#         ex += Frase[i]
# print(ex)

# # ex 9
# x = input('Valor que buscas: ')
# ex = 0
# for i in range(len(Frase)):
#     if Frase[i] == x:
#         ex+=1
# print(ex)

# # ex 10
# Frase = ('Frase de exemplo').lower()
# a = Frase[::-1]
# print(a)

# # ex 11
# Frase = ('Frase de exemplo')
# ac = ''
# for i in range(len(Frase)):
#     ac+= Frase[i]
#     print(ac)

# # ex 12
# Frase = ('Frase de exemplo')
# ind = 'aeiou '
# cont = 0
# for letra in Frase:
#     if letra in ind:
#         cont += 1
# print(cont)

# # ex 13
# Frase = input('Valor: ')
# a = 0
# for i in range(len(Frase)):
#     if Frase[i] == '-':
#         print(end='')
#     else:
#         a += 1
# print(a)
## ex 14 ab
# frase = 'Iracema – a lenda do Ceará'
# frase = frase.lower()
# frase_2 = ''
# for i in range(len(frase)):
#     if i == 0:
#         frase_2 = frase[i].upper()
#         print(end='')
#     else:
#         frase_2 += frase[i]
# print(frase_2)
# # ex 14c
# frase = 'Iracema – a lenda do Ceará'
# frase = frase.lower()
# frase_2 = ''
# for i in range(len(frase)):
#     if i == 0:
#         frase_2 = frase[i].upper()
#         print(end='')
#     if frase[i-1] == ' ':
#         frase_2 += frase[i].upper()
#     else:
#         frase_2+=frase[i]

# print(frase_2)

# # ex 14d
# frase = 'Iracema – a lenda do Ceará'
# f2 = ''
# flag = True
# for letra in frase:
#     if letra == ' ' and flag == True:
#         letra = '#'
#         flag = False
#     f2 += letra
# print(f2)

# # ex 14 e
# frase = 'Iracema – a lenda do Ceará'
# frase2 = frase[::-1]
# f2 = ''
# flag = True
# for letra in frase2:
#     if letra == ' ' and flag == True:
#         letra = '*'
#         flag = False
#     f2 += letra
# print(f2[::-1])

# # ex 14 f
# frase = 'Iracema – a lenda do Ceará'
# f2 = ''
# for letra in frase:
#     if letra == ' ':
#         letra = ''
#     f2 += letra
# print(f2)

# # ex 14 g
# frase = 'Iracema – a lenda do Ceará'
# i = 0
# f = True
# for letra in frase:
#     if letra == 'a' and f == True:
#         print(i)
#         f = False
#     i += 1

# # ex 14 h
# frase = 'Iracema – a lenda do Ceará'
# i = 0
# f = True
# i = len(frase)
# frase = frase[::-1]
# for letra in frase:
#     if letra == 'á':
#         letra = 'a'
#     if letra == 'a' and f == True:
#         print(i)
#         f = False
#     i -= -1

# # ex 14 i
# frase = 'Iracema – a lenda do Ceará'
# c = 0
# for i in frase:
#     if i == 'e':
#         c += 1
# print(c)

# # ex 14 j
# frase = 'Iracema – a lenda do Ceará'
# fra = ''
# maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in frase:
#     if i in maiuscula:
#         fra += i.lower()
#     else:
#         fra += i.upper()
# print(fra)

# # ex 15
# x = input('Sequencia de letras: ')
# ac = x[0]
# for valor in range(1,len(x)):
#     if x[valor] == x[valor-1]:
#         ac+= x[valor]
#     else:
#         print(ac)
#         ac = ''
#         ac += x[valor]
# print(ac)

# # ex 16
# x = input('Frase palindromo: ')
# y = x[::-1]
# p = True
# r = ''
# for i in range(len(x)):
#     if x[i] != y[i]:
#         p = False
#         r = 'Não'
#     if p == True:
#         r = 'Sim'
# print(r)

# # ex 17
# x = ('Subi no ônibus').lower()
# p = True
# r = ''
# Frase_tratada=''
# acentos_ag = 'óôò'
# for j in x:
#     if j == ' ':
#         j = ''
#     elif j in acentos_ag:                                                 #sem o elif temos a duplicação do 'o'
#         j = 'o'
#     Frase_tratada+=j
# print(Frase_tratada)

# y = Frase_tratada[::-1]

# for i in range(len(Frase_tratada)):
#     if Frase_tratada[i] != y[i]:
#         p = False
#         r = 'Não'
#     if p == True:
#         r = 'Sim'
# print(r)

# # ex 18
# x = ('roma')                            # se fosse romaa e amora não daria certo, pois não pegamos indices e sim caracteres
# y = ('amor')
# ac = ''
# y_usada = ''
# anagrama = True
# if len(x) > len(y) or len(y) > len(x):
#     anagrama = False
#     print('Não')
# else:
#     for i in range(len(x)):
#         for j in range(len(y)):
#             if y[j] == x[i] and y[j] not in y_usada:
#                 ac += '_'
#                 if y[j] not in y_usada:
#                     y_usada += y[j]
# print(ac)
# if len(ac) != len(x):
#     print('Não')
# else:
#     print('Sim')]
