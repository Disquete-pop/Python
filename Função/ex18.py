def Ord_maior(x):
    lista = []
    L2 = []
    maior = 0
    ind = 0
    for i in range(x):
        lista.append(int(input(f'Valor do indice {i}: ')))
        print(lista)
    while len(lista) != 0:
        maior = lista[0]
        ind = 0
        for i in range(len(lista)):
            if lista[i] > maior:
                maior = lista[i]
                ind = i
        L2.append(maior)
        del lista[ind]
    return L2

Y = int(input('Valor de indices: '))
A = Ord_maior(Y)
print(A)