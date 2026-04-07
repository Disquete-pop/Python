def existe(nomedicio):
    import os
    if os.path.exists(nomedicio):
        return True
    else:
        return False

def grava(nomedicio,dicio):
    if len(dicio):
        refarq = open(nomedicio,'w')
        for valor in dicio:
            chave = valor
            dvalor = ''
            for d in dicio[valor]:
                dvalor += dicio[valor][d] + '*'
            linha = chave + '\t' + d + '*' + dvalor + '\n'
            refarq.write(linha)
        refarq.close()

def le(nomedicio,dicio):
    if existe(nomedicio):
        refaqr = open(nomedicio,'r')
        for linha in refaqr:
            linha = linha[:len(linha)-2]
            dados = linha.split('\t')
            for i in dados:
                chave2 = ''
                if '*' in i:
                    chave2 = i
                    chave2 = chave2.split('*')
                    print(chave2)
                    dicio2 = {f'{chave2[0]}' : f'{chave2[1]}'}
            dicio[dados[0]] = dicio2
        refaqr.close()

nomearq = 'Dicio.txt'
dicio = {'chave_1' : {'topico 1' : 'programar' },
         'chave_2' : {'topico 2' : 'Deletar' }
         
        }

print(le(nomearq,dicio))
print(dicio)
print(grava(nomearq,dicio))