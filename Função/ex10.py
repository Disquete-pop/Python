def combinador(a,b):
    a = a
    b = b
    ac = ''
    for i in range(len(a)):
        ac += a[i] + b[i]
    return ac
print('As palavras devem ter o mesmo tamanho')
Frase_1 = input('Palavra 1: ')
Frase_2 = input('Palavra 2: ')
c = combinador(Frase_1,Frase_2)
print(c)