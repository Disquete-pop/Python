M = int(input('Valor de linhas: '))
N = int(input('Colunas: '))
mat= []
mat2=[]

for i in range(M):
    linha_atual = []
    for j in range(N):
        x = int(input(f'Valor de {[i]}{[j]} '))
        linha_atual.append(x)
    mat.append(linha_atual)
print('Matriz original')
for valor in mat:
    print(valor)

for i in range(N):
    linha_atual2 = []
    for j in range(M):
        linha_atual2.append(mat[j][i])
    mat2.append(linha_atual2)
print('Transposta')
for valor2 in mat2:
    print(valor2)