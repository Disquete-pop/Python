M = int(input('Linhas da matriz: '))
N = int(input('Colunas da matriz: '))
mat = []
for i in range(M):
    linhas = []
    for j in range(N):
        x = int(input(f'Informe o valor da matriz [{i}][{j}]: '))
        linhas.append(x)
    mat.append(linhas)
    print(mat)