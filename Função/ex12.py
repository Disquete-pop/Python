def listagem(N):
    lista = [0] * N
    ac = 0
    for i in range(len(lista)):
        lista[i] = float(input(f'Valor {i} da lista : '))
        ac += lista[i]
        print(lista)
    return ac
x = int(input('Numero de valores da lista: '))
A = listagem(x)
print(A)