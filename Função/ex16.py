# Faça uma função que recebe uma lista de números reais e retorna o valor do menor
# elemento e sua posição na lista. Não é permiƟdo o uso de qualquer função que não
# seja da sua autoria

def loc(N):
    lista = [0] * N
    flag = True
    menor_valor = 0
    ind = 0
    for i in range(len(lista)):
        lista[i] = float(input(f'Valor {i} da lista: '))
        print(lista)
        if flag == True:
            menor_valor = lista[i]
            ind = i
            flag = False
        if lista[i] < menor_valor:
            menor_valor = lista[i]
            ind = i
    return menor_valor,ind

x = int(input('Valor de indices da lista: '))
y = loc(x)
print(y)