lista = [0] * 15
lista_par = []
ac_par = 0
lista_impar = []
ac_impar = 0
for i in range(len(lista)):
    lista[i] = int(input('Valor: '))
    print(lista)
    if lista[i] %2 == 0:
        lista_par.append(lista[i])
        ac_par += lista[i]
    else:
        lista_impar.append(lista[i])
        ac_impar += lista[i]
print(f'Soma dos pares: {ac_par}')
print(f'Soma dos impares {ac_impar}')