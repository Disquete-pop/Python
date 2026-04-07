# # ex 1
# x = ('araraquara')
# z = x[1::2]
# a = x[::-2]
# print(z)
# print(a)
# frase = ''
# if len(a) > len(z):
#     for i in range(len(a)):
#         if i < len(z):
#             frase += a[i] + z[i]
#         else: 
#             frase += a[i]
#     print(frase)
# if len(z)>len(z):
#     for i in range(len(z)):
#         if i < len(a):
#                 frase += a[i] + z[i]
#         else: 
#             frase += z[i]
#     print(frase)
# if len(z) == len(a):
#     for i in range(len(a)):
#         frase += a[i] + z[i]
# print(frase)

# ex 2 
# x = "aaabbbcccccdddeeee"
# ac = ""
# for letra in x:
#     if letra not in ac:
#         ac += letra
# print(ac)

# x = "aaabbbcccdddeeee"
# ac = ""
# for letra in x:
#     if letra != ac[-1:]:
#         ac += letra

# # ex 3
# frase = 'roma'
# frase2  = 'amor'
# f1 = frase
# print(f1)
# f2 = frase2
# print(f2)
# ac = ''
# for i in range(len(f2)):
#     ac += f1[i] + f2 [i]
# print(ac)


# # ex 4  
# palavra = 'coiso'
# e ='abcdefghijklmnopqrstuvwxyz'
# b ='zyxwvutsrqponmlkjihgfedcba'
# ac = ''
# for i in palavra:
#     cont = 0
#     achou = False
#     for j in e:
#         cont +=1
#         if i == j and achou == False:
#             i = b[cont-1]
#             ac += i
#             achou = True
# print(ac)
 
# # ex 5
# a = 'frase teste'
# ac = ''
# for i in a:
#     if i not in ac:
#         ac +=i
# print(ac)

# # ex 6 
# a = 'frase teste'
# ac = ''
# c = 0
# ac2 = ''
# for i in a:
    
#     if c %2 == 0:
#         ac+= i
#     else:
#         ac2+=i
#     c += 1
# print(ac,ac2)

# # ex 7
# a = 'aaaabbbbcc'
# resumo = ''
# cont = 1
# for i in range(1,len(a)):
#     if a[i] == a[i-1]:
#         cont+=1
#     else:
#         resumo += a[i-1] + str(cont)
#         cont = 1
# resumo += a[-1] + str(cont)
# print(resumo)


'vtmnc string'