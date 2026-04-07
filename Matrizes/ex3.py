M = int(input('Linhas da matriz: '))
N = M
o = 0
ac = 0
mat = []
diag = []
for i in range(M):
    linhas = []
    for j in range(N):
        x = int(input(f'Informe o valor da matriz [{i}][{j}]: '))
        linhas.append(x)
    mat.append(linhas)
    print(mat)
for k in range(M):
    ac += mat[o][o]
    ad = mat[o][o]
    o += 1
    print(ad)
print(ac)