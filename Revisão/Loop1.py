# # Uso do for
#for i in range(0,valor+1):
    #+1 por conta do indice 0

# acumulador
'''Numero = int(input('Valor a ser acumulado: '))
acumulador = 0 # Dependendo da operação será 0 (Soma ou subtração) ou 1(Multiplicação ou divisão)
for i in range(0,Numero+1):
    acumulador += i
    print(acumulador)'''

#forial
'''Numero = int(input('Valor de quantas repetições: '))
acumulador = 1
for i in range(1,Numero+1):
    acumulador = acumulador * i # Segue a mesma ideia da soma
    print(acumulador)'''

# Pares e impares
Numero = int(input('Valores: '))
'''for i in range(1,Numero+1):
    if i % 2 ==0: # resto da divisão (Usar o exemplo papel)
        print(f'Par {i}')
    else:
        print(f'Impar {i}')'''

# Tabuada
'''Numero = int(input('Valor da tabuada: '))
x = int(input('Até onde vai: '))
valor = 0
for i in range(0,x+1):
    valor = Numero * i
    print(f'{Numero} X {i} = {valor}')'''