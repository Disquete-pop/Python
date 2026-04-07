# Produto de matriz é a linha da primeira pela coluna  M x P
m = int(input('Valor de M: ')) # linha
n = int(input('Valor de N: ')) # coluna
p = int(input('Valor de P: ')) # coluna
mat_1 = []
mat_2 = []
mat_2_Transposta = []
mat_3 = []
linha_m = []

for i in range(m):
    linha_atual = []
    for j in range(n):
        x = int(input(f'Valor de {[i]}{[j]}: '))
        linha_atual.append(x)
    mat_1.append(linha_atual)
print('Matriz 1')
for valor in mat_1:
    print(valor)

for i in range(n):
    linha_atual_2 = []
    for j in range(p):
        x = int(input(f'Valor de {[i]}{[j]}: '))
        linha_atual_2.append(x)
    mat_2.append(linha_atual_2)
print('Matriz 2')
for valor in mat_2:
    print(valor)
# transposta mat 2
for i in range(p):
    linha_atual_3 = []
    for j in range(n):
        linha_atual_3.append(mat_2[j][i])
    mat_2_Transposta.append(linha_atual_3)
print('transposta')
for valor in mat_2_Transposta:
    print(valor)

# for i in range(m):                 # linhas de A
#     linha_atual_4 = []
#     for j in range(p):             # colunas de B
#         soma = 0
#         for k in range(n):         # percorre elementos da linha e coluna
#             soma += mat_1[i][k] * mat_2_Transposta[j][k]
#         linha_atual_4.append(soma)
#     mat_3.append(linha_atual_4)
# print('Valor produto')
# for valor in mat_3:
#     print(valor)

# ver na aula...
