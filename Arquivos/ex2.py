# para saber se existe!
def existe(nomearq):
    import os
    if os.path.exists(nomearq):
        return True
    else:
        return False
#=============================   grava arquivo

def grava(nomearq,dicio):
    if len(dicio):
        ref_arq = open(nomearq,'w')
        for pessoa in dicio:
            dados = dicio[pessoa]
            linha = ( str(pessoa) + '\t' + dados['sexo'] + '\t' + str(dados['idade']) + '\t' + dados['fumante'] + '\t' + dados['regiao'] + '\t' + dados['escolaridade'] + '\n')
            ref_arq.write(linha)
            '''
            for chave in dicio:
            sexo = dicio[chave]["sexo"]
            idade = dicio[chave]["idade"]
            fumante = dicio[chave]["fumante"]
            regiao = dicio[chave]["regiao"]
            escolaridade = dicio[chave]["escolaridade"]

            linha = f"{chave}\t{sexo}\t{idade}\t{fumante}\t{regiao}\t{escolaridade}\n"
            ref_arq.write(linha)
            '''
    ref_arq.close()
    return 'Gravado com sucesso!'

#============================= lê o arquivo e reconstoi o dicionário

def lerarq(nomearq,dicio):
    if existe(nomearq):
        ref_arq = open(nomearq,'r')
        for linha in ref_arq:
            linha = linha[:len(linha)-1] # remove o \n
            dados = linha.split('\t')    # separa os campos

            chave = dados[0]
            sexo = dados[1]
            idade = dados[2]
            fumante = dados[3]
            regiao = dados[4]
            escolaridade = dados[5]

            dicio[chave] = {
                'sexo' : sexo,
                'idade' : idade,
                'fumante' : fumante,
                'regiao' : regiao,
                'escolaridade' : escolaridade
            }
        ref_arq.close()

#============================= fumantes %
def esc1(dicio):
    total_mulheres = 0
    total_homens = 0
    total_homens_fumantes = 0
    total_mulheres_fumantes = 0
    for valor in dicio:
        for item in dicio[valor]:
            if item == 'sexo' and dicio[valor][item] == 'F':
                total_mulheres += 1
                if dicio[valor]['fumante'] == 'sim':
                    total_mulheres_fumantes +=1
            elif item == 'sexo' and dicio[valor][item] == 'M':
                total_homens += 1
                if dicio[valor]['fumante'] == 'sim':
                    total_homens_fumantes +=1
    a = (f'Total de mulheres que fumam é {((total_mulheres_fumantes/total_mulheres)*100)}%')
    b = (f'Total de homens que fumam é {((total_homens_fumantes/total_homens)*100)}%')
    return a,b
#=============================

#============================= fumantes % região
def esc2(dicio):
    D2 = {}
    total_F = 0
    total_M = 0
    for valor in dicio:
        regiao = dicio[valor]['regiao']
        if regiao not in D2:
            D2[regiao] = {'F' : 0,
                            'Total Feminino' : 0,
                            'M' : 0,
                            'Total Masculino' : 0}
        if dicio[valor]['fumante'] == 'sim' and dicio[valor]['sexo'] == 'F':
            D2[regiao]['F'] += 1
        elif dicio[valor]['fumante'] == 'sim' and dicio[valor]['sexo'] == 'M':
            D2[regiao]['M'] += 1

        if dicio[valor]['sexo'] == 'M' and regiao in D2 :
            D2[regiao]['Total Masculino'] += 1
            total_M += 1
        else:
            D2[regiao]['Total Feminino'] += 1
            total_F += 1  
    for valor in D2:
        if D2[valor]['F'] != 0:
            D2[valor]['F'] = f'{(D2[valor]['F']/D2[valor]['Total Feminino'])*100}% Das mulheres'
        if D2[valor]['M'] != 0:
            D2[valor]['M']= f'{(D2[valor]['M']/D2[valor]['Total Masculino'])*100}% dos homens'
    for valor in D2:
        if type(D2[valor]['F']) == str and  D2[valor]['M'] == 0:
            D2[valor] = D2[valor]['F']
        elif type(D2[valor]['F']) == str and  type(D2[valor]['M']) == str:
            D2[valor] = (D2[valor]['F'],D2[valor]['M'],)
        elif D2[valor]['F'] == 0 and type(D2[valor]['M']) == str:
            D2[valor] = D2[valor]['M']
        elif D2[valor]['F'] == 0 and  D2[valor]['M'] == 0:
            D2[valor] = 'Ninguém Fuma! 0%'
    return D2
#=========================================
def esc3(dicio):
    M_total = 0
    mif = 0
    for valor in dicio:
        if dicio[valor]['sexo'] == 'M':
            M_total += 1
        if dicio[valor]['sexo'] == 'M' and dicio[valor]['idade'] < 40 and dicio[valor]['fumante'] == 'não' and dicio[valor]['escolaridade'] == 'ensino médio':
            mif += 1
    if M_total == 0:
        return ('Não há homens no dicionário!')
    else:
        res = (f'total de homens que não fumam, que tem ensino médio completo, com idade menor que 40 é {(mif/M_total)*100}%')
        return res
#========================================
def esc4(dicio):
    total_ = 0
    cont = 0
    for valor in dicio:
        if dicio[valor]['sexo'] == 'M' and dicio[valor]['fumante'] == 'sim' and dicio[valor]['escolaridade'] == 'superior':
            total_ += 1
        elif dicio[valor]['sexo'] == 'F' and dicio[valor]['fumante'] == 'sim' and dicio[valor]['escolaridade'] == 'superior':
            total_ += 1
        cont += 1
    res = (total_/cont)*100
    return res



nomearq = 'pesquisa.txt'
dc = {
    1: {
        "sexo": "F",
        "idade": 24,
        "fumante": "sim",
        "regiao": "sudeste",
        "escolaridade": "ensino médio"
    },
    2: {
        "sexo": "M",
        "idade": 33,
        "fumante": "não",
        "regiao": "norte",
        "escolaridade": "superior"
    },
    3: {
        "sexo": "F",
        "idade": 55,
        "fumante": "não",
        "regiao": "sudeste",
        "escolaridade": "superior"
    },
    4: {
        "sexo": "M",
        "idade": 18,
        "fumante": "sim",
        "regiao": "nordeste",
        "escolaridade": "ensino médio"
    }
}
lerarq(nomearq,dc)
esc = int(input('''
1 - Calcular e apresentar o percentual de fumantes homens e o percentual
de fumantes mulheres.
2- Calcular e apresentar o percentual total de fumantes por cada região (ou
seja, homens e mulheres)
3 - Calcular e apresentar o percentual de homens não fumantes abaixo de 40
anos e que cursaram até o nível médio, em relação ao número total de
homens entrevistados.
4 - Calcular e apresentar o percentual de mulheres e de homens fumantes
com ensino superior. 
0 - sair
Sua escolha é? '''))
while esc != 0:
    if esc == 1:
        print('\n Total de fumantes em %\n')
        print(esc1(dc))
        print('\n')
    elif esc == 2:
        for valor in esc2(dc):
            print(valor, ":",esc2(dc)[valor])
    elif esc == 3:
        print('\n')
        print(esc3(dc))
        print('\n')
    elif esc == 4:
        print('\n')
        print(esc4(dc))
        print('\n')
    esc = int(input('''
1 - Calcular e apresentar o percentual de fumantes homens e o percentual
de fumantes mulheres.
2- Calcular e apresentar o percentual total de fumantes por cada região (ou
seja, homens e mulheres)
3 - Calcular e apresentar o percentual de homens não fumantes abaixo de 40
anos e que cursaram até o nível médio, em relação ao número total de
homens entrevistados.
4 - Calcular e apresentar o percentual de mulheres e de homens fumantes
com ensino superior. 
0 - sair
Sua escolha é? '''))
grava(nomearq,dc)