N = int(input('Valor N: '))
lista = [0] * N
for i in range(len(lista)):
    lista[i] = int(input('Valor da lista: '))
    print(lista)
b = int(input('Valor que precura na lista: '))
if b in lista:
    print('Sim')
else:
    print('Não')