

def a(a,b,c,d):
    tupla = (a,b,c,d)
    return(tupla)
A = int(input('Inteiro '))
B = float(input('Float'))
C = input('str')
D = input('str')
res = a(A,B,C,D)
print(res)
'''
# ex 4
'''
def valor():
    a = int(input('Valor de valores da tupla: '))
    tupla = ()
    while a > 0:
        x = int(input("numero: "))
        tupla += (x,)
        a -= 1
    return tupla
print(valor())
'''
# ex 5
'''
def contador():
    tupla = ()
    tupla_2 = ()
    a = int(input('Num de textos: '))
    while a > 0:
        cont = 0
        x = str(input('Digite um texto'))
        tupla += (x,)
        a -= 1
    for valor in tupla:
        tupla_2 += (len(valor),)
    return tupla_2

print(contador())

# ex 20 
def coiso():
    t1 = ()
    cont = ''
    num = 0
    palavra = input('Palavra: ')
    for letra in palavra:
        if letra not in cont:
            for valor in palavra:
                if letra == valor:
                    num += 1
            t1 += ((letra,num),)
            num = 0
        cont += letra

    return(t1)
print(coiso())

# fazer com fatiamento e contagem dentro da propria tupla