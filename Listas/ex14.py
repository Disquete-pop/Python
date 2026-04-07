N = int(input('Escolha um numero inteiro: '))
lista =[0] * N
for i in range(len(lista)):
    lista[i] = int(input('Valor: '))
print(lista)
remover = int(input('Valor a ser removido '))
j = 0
while j < len(lista):
    if lista[j] == remover:
        del lista[j]
    else:
        j += 1
print(lista)