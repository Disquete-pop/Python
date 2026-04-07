def palavras(palavra):
    cont = 1
    for i in palavra:
        if i == ' ':
            cont += 1
    return cont

x = input('Escreva uma palavra: ')
p = palavras(x)
print(p)