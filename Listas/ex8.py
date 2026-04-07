N = int(input('Valor N: '))
lista = [0] * N
maior = 0
cont = 0
for i in range(len(lista)):
    lista[i] = int(input('Valor da lista: '))
    print(lista)
    if maior < lista[i]:
        maior = lista[i]
        cont = i
print(maior, cont)