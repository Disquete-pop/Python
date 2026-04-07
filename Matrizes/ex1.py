linhas = 3
colunas = 3
ac = 0
mat = []
ac2 = 0
for i in range(linhas):
    linha=[]
    ac2 = 0
    for j in range(colunas):
        x = int(input(f'Informe o numero [{i}][{j}]: '))
        linha.append(x)
        ac += x
        ac2 += x
    mat.append(linha)   # rever essa parte no slide
    print(mat)
    print(f'Soma total {ac}')
    print(f'Soma da linha {ac2}')