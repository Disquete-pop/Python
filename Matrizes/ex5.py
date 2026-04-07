linha = 2
coluna = 2
mat = []
mat2 = []
mat3 = []
print('Matriz 1')
for i in range(linha):
    linha_atual = []
    for j in range(coluna):
        x = int(input(f'Informe o valor da matris [{i}][{j}]'))
        linha_atual.append(x)
    mat.append(linha_atual)
for palavra in mat:
    print(palavra)
# matriz 2
print('Matriz 2')
for i in range(linha):
    linha_atual_2 = []
    for j in range(coluna):
        y = int(input(f'Informe o valor da matris [{i}][{j}]'))
        linha_atual_2.append(y)
    mat2.append(linha_atual_2)
for letra2 in mat2:
    print(letra2)
# nova 
print('Mtariz soma')

for i in range(linha):
    linha_atual_3 = []
    for j in range(coluna):
        z = mat[i][j] + mat2[i][j]
        linha_atual_3.append(z)
    mat3.append(linha_atual_3)
for letra3 in mat3:
    print(letra3)