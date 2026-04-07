#  Faça uma função que recebe uma lista de números reais e retorna o valor da média
# entre seus elementos. Não é permiƟdo o uso de qualquer função que não seja da
# sua autoria. 
def med(N):
    lista = [0] * N
    media = 0
    ac = 0
    media_elemento = 0
    for i in range(len(lista)):
        lista[i] = float(input(f'Valor {i} da lista: '))
        media += lista[i]
        ac += 1
        media_elemento = media/ac
    return media_elemento

X = int(input('Valor de indices da lista: '))
y = med(X)
print(y)