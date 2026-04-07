N = int(input('Escolha um numero inteiro: '))
lista =[0] * N
for i in range(len(lista)):
    lista[i] = int(input('Valor: '))
print(lista)

maior_qtd = 0           # maior quantidade encontrada até agora
mais_frequentes = []    # lista com os números mais frequentes

for i in range(len(lista)):
    contador = 0
    for j in range(len(lista)):
        if lista[i] == lista[j]:
            contador += 1

    # comparação depois de contar
    if contador > maior_qtd:
        maior_qtd = contador
        mais_frequentes = [lista[i]]   # zera a lista e guarda o novo campeão
    elif contador == maior_qtd and lista[i] not in mais_frequentes:
        mais_frequentes.append(lista[i])  # adiciona no caso de empate

print("Mais frequente(s):", mais_frequentes, "aparecendo", maior_qtd, "vezes")