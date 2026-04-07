# #ex1
# lista = [0] * 10
# ac = 0
# a = 0
# for i in range(len(lista)):
#     lista[i] = int(input('valor: ' ))
#     a += lista[i]
#     if lista[i] % 2==0:
#         ac += lista[i]
#     print(lista)
# print(a)
# print(ac)

# # ex 2
# n = int(input('Valor de itens: '))
# lista = [0] * n
# a = True
# menor = 0
# for i in range(len(lista)):
#     lista[i] = int(input('Valor: '))
#     if a == True:
#         menor = lista[0]
#         a = False
#     if lista[i] < menor:
#         menor = lista[i]
#     print(lista)
# print(menor)

# # ex 3
# lista = [0] * 7
# a = True
# ac = 0
# l = []
# for i in range(len(lista)):
#     lista[i] = int(input('Valor: '))
#     ac += lista[i]
#     print(lista)
# media = ac / 7
# print(media)
# for i in lista:
#     if i > media:
#         l.append(i)
# print(l)

# # ex 4
# la = [3, -5 ,23 ,-156, 9]
# lb = [-345, 8, 76, 44 ,-6]
# l10 = [7 ,-21 ,45 ,1 ,77 ,231 ,98 ,33 ,55 ,3]
# lc = []
# for i in range(len(l10)):
#     if i < 5:
#         la.append(i)
#     else:
#         lb.append(i)
# print(la)
# print(lb)
# for i in range(10):
#     lc.append(la[i]+lb[i])
# print(lc)

# # ex 5
# ListaA =[ 7, -21, 45, 1, 77, -5, 98, 3, 55, 31, 2, 10, 4, 1, 9]
# p = 0
# b = 0
# for i in range(len(ListaA)):
#     if ListaA[i] %2==0:
#         p+=ListaA[i]
#     else:
#         b+=ListaA[i]
# print(p,b)

# # ex 6
# ListaA =[ 7, -21, 45, 1, 77, -5, 98, 3, 55, 31, 2, 10, 4, 1, 9]
# inp = int(input('Valor: '))
# if inp in ListaA:
#     print('Sim')
# else:
#     print('Não')

# # ex 7
# n = int(input('Valor de listas: '))
# lis = [0] * n
# for i in range(len(lis)):
#     lis[i] = int(input(f'Valir de {i} da lsita: '))
#     print(lis)
# x = int(input('O que provuras? '))
# for i in range(len(lis)):
#     if x == lis[i]:
#         print(i)
# if x not in lis:
#     print(-1)

# ex 8
...
# # ex 9
# ListaA =[ 7, -21, 45, 1, 77, -5, 98, 3, 55, 31, 2, 10, 4, 1, 9]
# print(ListaA[::-1])

# # ex 10
# ListaA =[ 7, 1, 45, 1, 77, -5, 98, 3, 55, 31, 2, 10, 4, 1, 9]
# x = int(input('O que buscas? '))
# ac = 0
# for i in ListaA:
#     if i == x:
#         ac += 1
# print(ac)

# # ex 11
# ListaA =[ 1, 5, 1, 5, 1, 5, 98, 3, 55, 1, 2, 10, 4, 5, 9]
# ac = 0
# mai = 0
# lmai = [0]
# for i in range(len(ListaA)):
#     ac = 0
#     for j in range(len(ListaA)):
#         if ListaA[i] == ListaA[j]:
#             ac+=1
#     if ac > mai:
#         mai = ac
#         lmai = [ListaA[i]]
#     elif ac == mai:
#         if ListaA[i] not in lmai:
#             lmai.append(ListaA[i])
# print(lmai)

# # ex 12
# n = int(input('Valor de N: '))
# lista = [0] * n
# f = False
# for i in range(len(lista)):
#     lista[i] = int(input(f'Valor do indice {i} da lista: '))
#     print(lista)

# x = int(input('Valor que deseja remover da primera ocorrencia: '))
# lista2 = []
# for j in lista:
#     if j == x and f == False:
#         j = ''
#         f = True
#     else:
#         lista2.append(j)
# print(lista2)

# # ex 13
# n = int(input('Valor de N: '))
# lista = [0] * n
# f = False
# for i in range(len(lista)):
#     lista[i] = int(input(f'Valor do indice {i} da lista: '))
#     print(lista)

# x = int(input('Valor que deseja remover da ultima ocorrencia: '))
# lista3 = lista[::-1]
# lista2 = []
# for j in lista3:
#     if j == x and f == False:
#         j = ''
#         f = True
#     else:
#         lista2.append(j)
# print(lista2[::-1])

# #ex 14
# n = int(input('Valor de N: '))
# lista = [0] * n
# for i in range(len(lista)):
#     lista[i] = int(input(f'Valor do indice {i} da lista: '))
#     print(lista)

# x = int(input('Valor que deseja remover da primera ocorrencia: '))
# lista2 = []
# for j in lista:
#     if j == x:
#         j = ''
#     else:
#         lista2.append(j)
# print(lista2)

# # ex 15
# x = input('Inicializar a lista? se sim de enter, se não escreva fim ')
# menor=''
# maior=''
# l = []
# f = False
# while x != 'fim':
#     x = input('Escreva: ')
#     if x != 'fim'or '':
#         l.append(x)
#     if f == False:
#         menor = x
#         maior = x
#         f = True
#     if len(x) > len(maior):
#         maior = x
#     if len(x) < len(menor):
#         menor = x
# print(l)
# print(maior)
# print(menor)

# # ex 16:
# x = input('Inicializar a lista? se sim de enter, se não escreva fim ')

# l = []
# l2 = []
# frase_limpa = ''

# while x != 'fim':
#     x = input('Escreva: ')
#     if x != 'fim'or '':
#         l.append(x)
#         print(l)

# y = input('Caracter que deseja remover: ')
# for letra in l:
#     if frase_limpa != '':
#         l2.append(frase_limpa)
#     frase_limpa=''
#     for j in letra:
#         if j != y:
#             frase_limpa+=j
# print(l2)
        
# ex 17
print('1- Incluir contato e telefone')
print('2- Alterar um telefone de um contato')
print('3- Excluir um telefone de um contato')
print('4- Consultar os telefones de um contato')
print('5- Listar todos os contatos e seus respecƟvos telefones')
print('6 – FIM')
Agenda=['Contato 1', ['99876-5645','98798-3244'], 'Contato 2',['99786-5531']]
x = input('Escolha o valor: ')
# 1
if x == '1':
    print(Agenda)
    y = input('Nome de contato ou FIM para sair: ')
    if y not in Agenda and y != 'FIM':
        Agenda.append(y)
    else:
         print('Contato invalido: ')
    while y != 'FIM':
            cont = []
            while y != 'FIM':
                y = input('Contatos que deseja ou FIM para sair: ')
                if y != 'FIM':
                    cont.append(y)
            Agenda.append(cont)
    print(Agenda)

if x == '2':
    y = input('Nome do contato que deseja alterar: ')
    for i in range(len(Agenda)):
        if Agenda[i] == y:
                print(Agenda[i+1])
                for valor in Agenda[i+1]:
                    print(Agenda)
                    j = input('Numero do contato que deseja alterar')
                    if valor == j:
                        valor = ''
                        k = input('Novo numero: ')
                        Agenda[i+1].append(k)
    print(Agenda)

if x == '3':
    y = input('Nome do contato que deseja alterar: ')
    for i in range(len(Agenda)):
        if Agenda[i] == y:
                print(Agenda[i+1])
                for valor in range(len(Agenda[i+1])):
                    print(Agenda)
                    j = input('Numero do contato que deseja alterar')
                    if Agenda[i+1][valor] == j:
                        k = input('Novo numero: ')
                        Agenda[i+1][valor] = k
                        print('Numero alterado!')
    print(Agenda)

if x == '4':
    y = input('Nome do contato que deseja Consultar: ')
    if y != 'FIM':
        for i in range(len(Agenda)):
            if Agenda[i] == y:
                    for valor in Agenda[i+1]:
                        print(valor, end=' ')
if x == '5':
    nomes = Agenda[::2]      # ['Contato 1', 'Contato 2']
    numeros = Agenda[1::2]   # [['99876-5645','98798-3244'], ['99786-5531']]

    for i in range(len(nomes)):
        print("Contato:", nomes[i])
        print("Números:", numeros[i])

if x == '6':
     print('Fim')
