def contador(palavra):
    valor = 0
    for i in palavra:
        if i != ' ':
            valor += 1
    return valor

x = input('Escreva algo: ')
cont = contador(x)
print(cont)