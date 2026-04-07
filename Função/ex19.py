def pali(f):
    
    f = f
    f = f.lower()
    f_2 = f[::-1]

    if f == f_2:
        x = True
    else:
        x = False
    return x

A = input('Verificador de palindromo: ')
b = pali(A)
print(b)