def contador(x):
    y = 0
    cont = 0
    if x < 0:
        x = x * (-1)
    if x > 0:
        while x > 0:
            y = x % 10
            x = x // 10
            cont +=1
    return cont


valor = int(input('Valor: '))
v2 = contador(valor)
print(v2)