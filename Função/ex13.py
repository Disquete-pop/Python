# Faça uma função que recebe uma lista de números reais e retorna o valor do
# produto desses números. Não é permitido o uso de qualquer função que não seja
# da sua autoria.
def prod(N):
    ac = 1
    lista = [0] * N
    for i in range(len(lista)):
        lista[i] = float(input('Valor da lista {i}: '))
        ac = ac * lista[i]
    return ac

A = int(input('Valor de elementos das lista: '))
x = prod(A)
print(x)