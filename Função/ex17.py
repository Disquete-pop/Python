# . Faça uma função que recebe uma lista de números reais e retorna a lista ordenada
# do menor para o maior valor. Não é permiƟdo o uso de qualquer função que não
# seja da sua autoria. 

def loc(N):
    lista = [0] * N
    lista_or = []
    menor_valor = 0
    ind = 0
    for i in range(len(lista)):
        lista[i] = float(input(f'Valor {i} da lista: '))
        print(lista)
    while len(lista) != 0:
        ind = 0
        menor_valor = lista[0]
        for i in range(len(lista)):
            if lista[i] < menor_valor:
                menor_valor = lista[i]
                ind = i
        lista_or.append(menor_valor)
        del lista[ind]
    return lista_or

    

x = int(input('Valor de indices da lista: '))
y = loc(x)
print(y)