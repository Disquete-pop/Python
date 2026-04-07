def existe(nomearq):
    import os
    if os.path.exists(nomearq):
        return True
    else:
        return False

def grava(nomearq,dicio):
    if len(dicio):
        refarq = open(nomearq,'w')
        for chave in dicio:
            lista = dicio[chave]
            primeira_lista = ''
            for i in lista:
                if type(i) != list:                           # uso do type
                    primeira_lista += '*'+ str(i) 
                else:
                    primeira_lista += '*'
                    f = False
                    for valor in i:
                        if f == False:
                            primeira_lista +=str(valor)
                            f = True
                        else:
                            primeira_lista +='\t'+ str(valor)

            linha = str(chave) + primeira_lista + '\n'
            refarq.write(linha)
        refarq.close()
        return 'Gravado'

def ler(nomearq,dicio):
    if existe(nomearq):
        refarq = open(nomearq)
        for linha in refarq:
            linha = linha[:len(linha)-1]
            linha = linha.split('*')
            linha2 = ''
            lista = []
            for i in linha:
                if '\t' in i:
                    linha2 = ''
                    linha2 += i
                    linha2 = linha2.split('\t')
                    corrigido = []
                    for j in linha2:
                        corrigido.append(int(j))
                    lista.append(corrigido)
                else:
                    lista.append(int(i))
                                                               # achar indice para dar split keqw feito!!!!
            dicio[str(lista[0])] = lista[1:]
            print(dicio)
        refarq.close()
        return 'lido'
    

    '''
    dicio = { chave : [lista1,[lista2]]
    }
    '''
dicio = { '1' : [1,2,3,[4,5,6]]}
nomearq = 'zecavera.txt'
ler(nomearq,dicio)
for valor in dicio:
    print(valor,':',dicio[valor])
grava(nomearq,dicio)
