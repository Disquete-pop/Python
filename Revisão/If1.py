# # ex 1
# a = int(input('Valor 1: '))
# b = int(input('Valor 2: '))
# c = a + b
# print(c)

# # ex 2
# a = int(input('Valor 1: '))
# b = int(input('Valor 2: '))
# c = (a+b)/2
# print(c)

# # ex 3
# nome = input('Nome: ')
# a = int(input('Valor 1: '))
# b = int(input('Valor 2: '))
# c = (a+b)/2
# print(f'A Media da {nome} é {c}')

# # ex 4
# a = int(input('Valor: '))
# print(f'Valor: {a} sucessor {a+1} e antecessor {a-1}')

# # ex 5
# a = int(input('Valor 1: '))
# b = int(input('Valor 2: '))
# c = int(input('Valor 3: '))
# media = ((a * 1) + (b * 2) + (c * 3))/(1+2+3)
# print(media)

# # ex 6
# x = int(input("Valor 1: "))
# y = int(input("Valor 2: "))
# z = ((x**2) + (y**2)) / ((x - y) * (x - y))
# print(z)

# # ex 7
# salario = int(input('Salario: '))
# aj = (salario) / 4
# reajuste = salario + aj
# print(reajuste)

# # ex 8
# x = int(input('Pressão desejada: '))
# y = int(input('Pessão da bomba '))
# z = x - y
# print(f'Para chegar na pressão desejada {x} deve-se {z} na pressão. ')

# # ex 9
# a = int(input('Tomada 1: '))
# b = int(input('Tomada 2: '))
# c = int(input('Tomada 3: '))
# d = int(input('Tomada 4: '))
# e = (a-1) + (b-1) + (c-1) + (d)
# print(e)

# # ex 10
# a = int(input('Valor 1: '))
# b = int(input('Valor 2: '))
# if a > b:
#     print(f'{a} é o maior valor')
# else: 
#     print(f'{b} é o maior valor')

# # ex 11
# a = int(input('Valor 1: '))
# b = int(input('Valor 2: '))

# if a > b:
#     print(b,a)
# else:
#     print(a,b)

# # ex 12
# a = int(input('0 ou 1 '))
# if a == 1:
#     print('C')
# if a == 0:
#     b = int(input('0 ou 1 '))
#     if b == 1:
#         print('B')
#     else:
#         print('A')

# ex 13
# Livros = int(input('Quantidade de livros: '))
# criterios = input('Criterios A ou B ').upper()
# total = 0
# if criterios == 'A':
#     total = (0.2 * Livros) + 7.5
#     print(total)
# if criterios == 'B':
#     total = (0.5 * Livros) + 2.5
#     print(total)

# # ex 14
# a = int(input('Valor de A: '))
# b = int(input('Valor de B: '))
# c = int(input('Valor de C: '))

# delta = (b**2) - (4*a*c)
# print(delta)
# x1 = ((-b) + (delta**(1/2))) / (2*a)
# x2 = ((-b) - (delta**(1/2))) / (2*a)
# print(f'Valor de X1 {x1}')
# print(f'Valord e x2 {x2}')

# # ex 15
# Nota = int(input('Valor da nota: '))
# if 100 >= Nota >= 86:
#     print('A')
# if 61 <= Nota <= 85:
#     print('B')
# if 36 <= Nota <= 60:
#     print('C')
# if 1 <= Nota <= 35:
#     print('D')
# if Nota == 0:
#     print('E')

# # ex 16
# a = int(input('Valor 1: '))
# b = int(input('Valor 2: '))
# c = int(input('Valor 3: '))
# if a < b < c:
#     print(a,b,c)
# if a < c < b:
#     print(a,c,b)
# if b < a < c:
#     print(b,a,c)
# if b < c < a:
#     print(b,c,a)
# if c < b < a:
#     print(c,b,a)
# if c < a < b:
#     print(c,a,b)

# # ex 17

# # ex 18
# x = int(input('Qual sua idade: '))
# if 16 <= x and x <= 17:
#     print('Facultativo')
# if 18 <= x <= 65:
#     print('Obrigatório')
# if x > 65:
#     print('Dispensado')

# # ex 18:

# x = int(input('Valor da compra: '))
# if x <= 100:
#     x2 = (x) - (x * (5/100))
#     print(x2)
# if 100 < x < 200:
#     x2 = (x) - (x * (10/100))
#     print(x2)
# if x >= 200:
#     x2 = (x) - (x * (20/100))
#     print(x2)
