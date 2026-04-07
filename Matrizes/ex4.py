linha = int(input('Valor: '))
coluna = linha
mat = []
for i in range(linha):
    linha_atual = []
    for j in range(coluna):
        x = int(input(f'Informe o valor da matris [{i}][{j}]'))
        linha_atual.append(x)
    mat.append(linha_atual)

for valor in mat:
    print(valor)
print('\n')
for i in range(linha):
    for j in range(coluna):
        if i == j:
            mat[i][j] = 1
        else:
            mat[i][j] = 0
for valor in mat:
    print(valor)
'''for linha in mat:             # forma mais simples de ver a
    print(linha) '''
# for i in range(mat):
#     for j in range(coluna):
#         if j == i:
#             mat[j][j] = 1
#         else:
#             mat[j][j] = 0
#     print(mat)
