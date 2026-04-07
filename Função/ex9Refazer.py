def num(Valor):
    lista_Unidade = [0,1,2,3,4,5,6,7,8,9,]
    Lista_Dezenas = [0,1,2,3,4,5,6,7,8,9]
    y = 0
    cont = 0
    unidade = 0
    dezena = 0
    uni = ''
    dez = ''
    while Valor > 0:
        y = Valor % 10
        Valor = Valor// 10
        if cont == 0:
            unidade = y
        if cont == 1:
            dezena = y
        cont +=1
    if unidade in lista_Unidade:
        if unidade == 0:
            uni = ' '
        if unidade == 1:
            uni = ' um'
        if unidade == 2:
            uni = ' dois'
        if unidade == 3:
            uni = ' tres'
        if unidade == 4:
            uni = ' quatro'
        if unidade == 5:
            uni = ' cinco'
        if unidade == 6:
            uni = ' seis'
        if unidade == 7:
            uni = ' sete'
        if unidade == 8:
            uni = ' oito'
        if unidade == 9:
            uni = ' nove'
    if dezena in Lista_Dezenas:
        if dezena == 0:
            dez = ' '
        if dezena == 1 and unidade == 0:
            dez = 'dez'
            uni= ' '
        if dezena == 1 and unidade == 1:
            dez = 'onze'
            uni= ' '
        if dezena == 1 and unidade == 2:
            dez = 'doze'
            uni= ' '
        if dezena == 1 and unidade == 3:
            dez = 'treze'
            uni= ' '
        if dezena == 1 and unidade == 4:
            dez = 'quatorze'
            uni= ' '
        if dezena == 1 and unidade == 5:
            dez = 'quinze'
            uni= ' '
        if dezena == 1 and unidade == 6:
            dez = 'dezeseis'
            uni= ' '
        if dezena == 1 and unidade == 7:
            dez = 'dezesete'
            uni= ' '  
        if dezena == 1 and unidade == 8:
            dez = 'dezoito'
            uni= ' ' 
        if dezena == 1 and unidade == 9:
            dez = 'dezenove'
            uni= ' ' 
        if dezena == 2:
            dez = 'vinte e'
        if dezena == 3:
            dez = 'trinta e'
        if dezena == 4:
            dez = 'quarenta e'
        if dezena == 5:
            dez = 'cinquenta e'
        if dezena == 6:
            dez = 'sessenta e'
        if dezena == 7:
            dez = 'setenta e'
        if dezena == 8:
            dez = 'oitenta e'
        if dezena == 9:
            dez = 'noventa e'
    d = dez+uni
    return d


X = int(input('Valor de 0 a 99: '))
Est = num(X)
print(Est)
