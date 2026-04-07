lista = [0] * 10
print(lista)
lista2 = []
soma_total = 0
for i in range(len(lista)):
    lista[i] = int(input('Valor: '))
    print(lista)
    soma_total+=lista[i]
    if lista[i] %2 ==0:
        lista2.append(lista[i])
print(f'soma dos valores: {soma_total}')
print(f'Valores pares {lista2}')