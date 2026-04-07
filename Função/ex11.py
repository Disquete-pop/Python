def pot(x,y):
    ac = 1
    while y > 0:
        ac = ac * x
        y -= 1
    return ac

a = int(input('Base: ')) 
b = int(input('Expoente: '))
resu = pot(a,b)
print(resu)