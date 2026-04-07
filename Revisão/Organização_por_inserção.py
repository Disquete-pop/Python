lista = [5, 25, 4, 60, 1, 30]
for i in range(1, len(lista)):
    chave = lista[i]  # Elemento atual a ser inserido
    j = i - 1

    # Move os elementos maiores que a chave uma posição à frente
    while j >= 0 and lista[j] > chave:
        lista[j + 1] = lista[j]
        j -= 1

    # Coloca a chave na posição correta
    lista[j + 1] = chave
print(lista)