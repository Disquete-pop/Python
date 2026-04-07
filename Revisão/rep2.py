# # ex 1
# n = int(input('Valor 1: '))
# m = int(input('Valor 2: '))
# if n > m:
#     while n > m:
#         print(n)
#         n -= 1
#     print(m)

# if m > n:
#     while m > n:
#         print(m)
#         m -= 1
#     print(n)

# # ex 2
# n = int(input('Base: '))
# m = int(input('expoente: '))
# ac = 1
# while m > 0:
#     ac = ac * n
#     m -= 1
# print(ac)

## ex 3
#n = int(input('N: '))
#i = int(input('I: '))
#j = int(input('J: '))
#cont = 0
#x = 0
#while cont < n :
#    if x % i == 0 or x % j == 0:
#        cont += 1
#        print(x)
#    x += 1

## ex 4
#num = int(input('Valor: '))
#x = 0
#ac = 0
#while num > 0:
#    x = num % 10
#    num = num // 10
#    if x % 2 == 0:
#        ac += x
#print(ac)

## ex 5
#num = int(input('Valor: '))
#x = 0
#ac = 0
#a = 1
#while num > 0:
#    x = num % 10
#    num = num // 10
#    if a % 2 == 0:
#        ac += x
#    a += 1
#print(ac)
        
## ex 6
#num = int(input('Valor: '))
#cont_par = 0
#cont_impar = 0
#while num > 0:
#    x = num % 10
#    num = num // 10
#    if x % 2 == 0:
#        cont_par += 1
#    else:
#        cont_impar += 1
#print(f'Pares: {cont_par}')
#print(f'Impares: {cont_impar}')

# ex 7 
#a = 1
#b = 1
#ac = a/b
#
#while a < 99:
#    a = a + 2
#    b = b + 1
#    ac += a/b
#print(ac)

# ex 7b
#a = 2
#b = 1
#c = 50
#ac = (a**b)/ 50
#while b < 50:
#    b += 1
#    c -= 1
#    ac += (a**b)/c
#print(ac)
    

# # ex 8
# n = 3
# mair_volta = 0
# i = 0
# media = 0
# ac = 0
# m = 3
# while n > 0:
#     a = int(input('Valor da volta: '))
#     if n == 3:
#         mair_volta = a
#         i = n
#     if a < mair_volta:
#         mair_volta = a
#         i = n
#     ac += a
#     n -= 1
# media += ac / m
# print(f'Melhor tempo: {mair_volta}')
# print(f'A volta de melhor tempo: {i}')
# print(f'Tempo médio das {m} voltas: {media}')







    




