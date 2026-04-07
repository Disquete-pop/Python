# Faça uma função que recebe uma lista de números reais e retorna o valor do maior
# elemento e sua posição na lista. Não é permiƟdo o uso de qualquer função que não
# seja da sua autoria.
def loc(N):
    lista = [0] * N
    maior_valor = 0
    ind = 0
    for i in range(len(lista)):
        lista[i] = float(input(f'Valor {i} da lista: '))
        print(lista)
        if lista[i] > maior_valor:
            maior_valor = lista[i]
            ind = i
    return maior_valor,ind

x = int(input('Valor de indices da lista: '))
y = loc(x)
print(y)