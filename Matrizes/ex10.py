# 10. Faça um programa que leia duas matrizes quadradas (A e B) de ordem informada
# pelo usuário e verifique se B é a matriz inversa de A. Mostre uma mensagem
# amigável ao usuário.
A = 3
B = 3
A_mat = []
B_mat = []
C_mat = []
D_mat = []
f = True
for i in range(A):
    linha_atual = []
    for j in range(B):
        X = int(input(f'Valor {i}{j}: '))
        linha_atual.append(X)
    A_mat.append(linha_atual)
for valor in A_mat:
    print(valor)

for i in range(A):
    linha_atual3 = []
    for j in range(B):
        z = A_mat[j][i]
        linha_atual3.append(z)
    C_mat.append(linha_atual3)
for valor in C_mat:
    print(valor)

for i in range(A):
    linha_atual4 = []
    for j in range(B):
        y = int(input(f'Valor {i}{j}: '))
        linha_atual4.append(y)
    B_mat.append(linha_atual4)
for valor2 in B_mat:
    print(valor2)

for i in range(A):
    linha_atual4 = []
    for j in range(B):
        if C_mat[i][j] == B_mat[i][j]:
            Flag = 'True'
            linha_atual4.append(Flag)
        else:
            Flag = 'False'
            linha_atual4.append(Flag)
    D_mat.append(linha_atual4)
for valor in range(A):
    for j in range(B):
        if C_mat[i][j] != B_mat[i][j]:
            f = False

if f == True:
    print('é')
else:
    print('Num é')