linhas = 3
colunas = 3
mat = []
for i in range(linhas):
    linha=[]
    for j in range(colunas):
        x = int(input(f'Informe o numero [{i}][{j}]: '))
        linha.append(x)
    mat.append(linha)   # rever essa parte no slide
    print(mat)
    # para printar em formato matricial
for i in range(linhas):
    for j in range(colunas):
      print(mat[i][j], end=' ')
    print()