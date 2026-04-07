# # ex1
# n = int(input('Valor: '))
# for i in range(1,n+1):
#     print(i, end=' ')

# # ex 2
# n = int(input('Valor: '))
# m = int(input('Valor: '))
# if n < m:
#     for i in range(n,m+1):
#         print(i, end=' ')
# if m < n:
#     for i in range(m,n+1):
#         print(i, end=' ')

# # ex 3
# n = 100
# ac = 0
# while n > 0:
#     ac += n
#     n = n - 1
# print(ac)

# # ex 4
# n = 100
# ac = 0
# while n > 0:
#     if n %2 == 0:
#         ac += n
#     n = n - 1
# print(ac)

# # ex 5
# chico = 150
# ze = 110
# anos = 0
# while chico > ze:
#     chico += 2
#     ze+= 3
#     anos += 1
# print(anos/10) 

# # ex 6
# n = int(input('Valor'))
# for i in range(0,11):
#     m = i * n
#     print(f'{i} x {n} = {m} ')

# # ex 7
# n = int(input('Valor: '))
# x = 1
# ac = 0
# while n > 0:
#     ac += x/n 
#     n = n - 1
# print(ac)

# # ex 8
# x = int(input('Valor: '))
# y = x
# ac = 1
# while y > 1:
#     ac = ac * x
#     x = x - 1
#     y -= 1
# print(ac)

# # ex 9
# x = int(input('Valor: '))
# maior_valor = x
# while x > 0:
#     if x > maior_valor:
#         maior_valor = x
#     x = int(input('Valor: '))
# print(maior_valor)

# # ex 10
# x = float(input('Nota do tralha: '))
# notas = []
# maior_nota = x
# menor_nota = x
# contador = 1
# while x > 0:
#     if maior_nota > x:
#         maior_nota = x
#     if menor_nota < x:
#         menor_nota = x
#     notas.append([x,f'Aluno {contador}'])
#     x = float(input('Nota do tralha: '))
#     contador += 1
# print(notas)
# print(f'Menor nota {menor_nota}')
# print(f'Maior nota {maior_nota}')

# # ex 11
# x = float(input('Nota do tralha: '))
# Notas_6 = 0
# Notas_4e6 = 0
# Notas_menor_que_4 = 0
# while x > 0:
#     if x >= 6:
#         Notas_6 += 1
#     if 4 <= x < 6:
#         Notas_4e6 += 1
#     if x < 4:
#         Notas_menor_que_4 +=1
#     x = float(input('Nota do tralha: '))
# print(f'Notas maiores ou iguais a 6: {Notas_6}')
# print(f'Notas maiores ou iguais a 4 e maiores que 6: {Notas_4e6}')
# print(f'Notas menores que 4: {Notas_menor_que_4}')

# # ex 12 Fibbo
# x = int(input('Valor de Fibbo: '))
# a = 1
# b = 1
# c = 2
# d = 0
# print(a,end=',')
# print(b,end=',')
# print(c,end=',')
# while x > 3:
#     d = b + c
#     if x > 4:
#         print(d, end=',')
#     if x == 4:
#         print(d)
#     b = c
#     c = d
#     x -= 1 

# # ex 13
# x = int(input('valor: '))
# while x > 1:
#     if x %2==0:
#         x = x/2
#     else:
#         x = 3 * x + 1
#     print(x, end=' ')

# # ex 15
# vagas = 0
# muié = 0
# homi = 0
# codigo = int(input('Codigo de curso: '))
# total_condidatos_universidade = 0
# maiornv_total = 0
# cod = 0
# flag = True
# while codigo != 0:
#     vagas = int(input('Vagas: '))
#     muié = int(input('Muies: '))
#     homi = int(input('Homis: '))
#     n_vtotal = (homi + muié) / vagas
#     fem = (muié / (homi + muié)) * 100
#     if flag == True:
#         maiornv_total = n_vtotal
#         flag = False
#         cod = codigo
#     if n_vtotal > maiornv_total:
#         maiornv_total = n_vtotal
#         cod = codigo
#     total_condidatos_universidade += (muié + homi)
#     print(f'Curso {codigo}: {n_vtotal:.2f} candidatos/vaga, {fem:.2f}% de mulheres')
#     print(f'\nMaior concorrência: {maiornv_total:.2f} candidatos/vaga (curso {cod})')
#     print(f'Total de candidatos na universidade: {total_condidatos_universidade}')
#     codigo = int(input('Codigo de curso: '))
