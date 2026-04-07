lista = int(input('Numero de pessoas: '))
a = [0] * lista
flag = True
menor = 0
for i in range(len(a)):
    a[i] = float(input('Altura '))
    print(a)
    if flag == True:
        menor = a[i]
        flag = False
    if menor > a[i]:
        menor = a[i]
print(a)
print(f'menor altura: {menor}')