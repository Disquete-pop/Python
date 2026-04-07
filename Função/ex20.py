def anagrama(a,b):
    flag =True
    lista_a = []
    lista_b = []
    for i in a:
        lista_a.append(i)
    for j in b:
        lista_b.append(j)
    for i in range(len(lista_a)):
        for j in range(len(lista_b)):
            if lista_a[i] == lista_b[j]:
                lista_b[j] = ''
                lista_a[i] = ''

    for j in lista_b:
        if j != '':
            flag = False
    return flag

x = input('Frase 1: ')
y = input('Frase 2: ')
Ana = anagrama(x,y)
print(Ana)