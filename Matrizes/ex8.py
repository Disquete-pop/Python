m = int(input('Linha '))
n = int(input('Colunas '))
mat = []
mat2 = []
mat3 = []
for i in range(m):
    linha_atual = []
    for j in range(n):
        x = int(input(f'Valor de {[i]}{[j]}: '))
        linha_atual.append(x)
    mat.append(linha_atual)
print('Matriz 1')
for valor in mat:
    print(valor)

for i in range(m):
    linha_atual2 = []
    for j in range(n):
        x2 = int(input(f'Valor de {[i]}{[j]}'))
        linha_atual2.append(x2)
    mat2.append(linha_atual2)
print('Matriz 2')
for valor in mat2:
    print(valor)

for i in range(m):
    linha_atual3 = []
    for j in range(n):
        linha_atual3.append(mat[i][j] - mat2[i][j])
    mat3.append(linha_atual3)
print('Resultante')
for valor in mat3:
    print(valor)