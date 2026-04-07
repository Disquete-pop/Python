lista = []
x = ''
cont = 0
flag = True
nova_lista = ''
Lista2 = []
while x != 'fim':
    x = input('String: ')
    if x != 'fim':
        lista.append(x)
    print(lista)    
    cont += 1
y = input('Deseja remover ')
for palavra in lista:
    if nova_lista != '':
        Lista2.append(nova_lista)
    nova_lista = ''
    for j in palavra:
        if j != y:
            nova_lista+=j
    print(Lista2)