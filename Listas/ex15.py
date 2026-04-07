lista = []
X = ''
cont = 0
maior_str = ''
menor_str = ''
flag = True
while X != 'fim':
    X = input('Escreva: ')
    lista.append(X)
    print(lista)
    if flag == True:
        maior_str = X
        menor_str = X
        flag = False
    if len(lista[cont]) > len(maior_str) and X != 'fim':
        maior_str = lista[cont]
    if len(lista[cont]) < len(menor_str) and X != 'fim':
        menor_str = lista[cont]
    cont += 1
print(lista)
print(f'Maior string: {maior_str}')
print(f'Menor string: {menor_str}')