lista = [0] * 7
media = 0
ac_temp = 0
ac = 0
lista2 = []
for i in range(len(lista)):
    lista[i] = float(input('Temperatura: '))
    ac += 1
    ac_temp += lista[i]
    media = ac_temp / ac
    print(lista)
    if lista[i] > media:
        lista2.append(lista[i])
print(lista)
print(f'Temperaturas acima da media: {lista2}')
