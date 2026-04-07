# Lista A: 3 -5 23 -156 9
# Lista B: -345 8 76 44 -6
# Lista_10: 7 -21 45 1 77 231 98 33 55 3
# Lista A: 3, -5, 23, -156, 9, 7, -21, 45, 1, 77
# Lista B: -345, 8, 76, 44, -6, 231, 98, 33, 55, 3
# Lista C: -342, 3, 99, -112, 3, 238, 77, 78, 56, 80
lista_a = [0] * 5
lista_b = [0] * 5
lista_10 = [0] * 10
lista_c = [0] * 10
for i in range(len(lista_a)):
    lista_a[i] = int(input('Valor da lista A '))
    print(lista_a)
for i in range(len(lista_b)):
    lista_b[i] = int(input('Valor da lista B '))
    print(lista_b)
for i in range(len(lista_10)):
    lista_10[i] = int(input('Valor da lista 10 '))
    print(lista_10)
for i in range(len(lista_10)):
    if i > 4:
        lista_b.append(lista_10[i])
    else:
        lista_a.append(lista_10[i])
    print(lista_a)
    print(lista_b)
for i in range(len(lista_c)):
    lista_c[i] = (lista_a[i]) + (lista_b[i])
    print(lista_c)