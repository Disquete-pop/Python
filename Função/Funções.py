#soma de dois numero
# area de funçãop deve ser antes do codigo

#Area de função
def soma():
    n1 = int(input("Valor 1"))       # funciona mas não queremos pois isso requer chamar a função
    n2 = int(input("Valor 2 "))      # Isso é uma função sem parametros
    res = n1 + n2
    print(f'A soma é {res}')
soma()     # isso é chamar


#programa principal
num1 = int(input("Valor 1"))
num2 = int(input("Valor 2 "))
res = num1 + num2
print(f'A soma é {res}')

# parametro

def soma(n1,n2):                                               # na lista a coisa muda
    res = n1 + n2
    # não se coloca print na função coloca-se return
    return res   # Atribui valor a variavel

# função com parametros / Principal
num1 = int(input("Valor 1"))
num2 = int(input("Valor 2 "))
resultado = soma(num1,num2)
print(f'A soma é {resultado}')


# não usar variavel global
# global, tudo que esá no principal
# local é o que está na função
