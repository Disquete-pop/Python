N = int(input('Escolha um numero inteiro: '))
lista =[0] * N
for i in range(len(lista)):
    lista[i] = int(input('Valor: '))
print(lista)
remover = int(input('Valor a ser removido '))
flag = True
j = 0
while j < len(lista):
    if lista[j] == remover and flag == True:
        del lista[j]
        flag = False
    else:
        j += 1
print(lista)