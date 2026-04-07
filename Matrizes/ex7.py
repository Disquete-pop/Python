mat = []
mat2 = []
mat3 = []
linha = 3
coluna = 3
resultado = 'Não'
for i in range(linha):
    linha_atual = []
    for j in range(coluna):
        x = int(input(f'Valor de {[i]}{[j]}: '))
        linha_atual.append(x)
    mat.append(linha_atual)
print('Matriz normal')
for valor in mat:
    print(valor)

for i in range(coluna):
    linha_atual2 = []
    for j in range(linha):
        linha_atual2.append(mat[j][i])
    mat2.append(linha_atual2)
print('Matrix transpoista')
for valor2 in mat2:
    print(valor2)

for i in range(linha):
    for j in range(coluna):
        if mat[i][j] == mat2[i][j]:
            resultado = 'Matriz Simetrica'
            mat3.append(resultado)
        else:
            resultado = 'Matriz Não é simetrica'
            mat3.append(resultado)
if 'Matriz Não é simetrica' in mat3:
    print('Matriz Não é simetrica')
else:
    print('Matriz Simetrica')
