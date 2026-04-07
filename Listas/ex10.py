N = int(input('Escolha um numero inteiro: '))
lista =[0] * N
for i in range(len(lista)):
    lista[i] = int(input('Valor: '))
    print(lista)
Buscador = int(input('Qual valor buscar na lista: '))
contador = 0
for i in range(len(lista)):
    if lista[i] == Buscador:
        contador += 1
print(f'O valor {Buscador} apareceu {contador} vezes. ')