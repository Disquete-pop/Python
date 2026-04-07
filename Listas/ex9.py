n = int(input('Valor de n: '))
lista = [0] * n
for i in range(len(lista)):
    lista[i] = int(input('Valor da lista: '))
    print(lista)
print(lista[::-1])