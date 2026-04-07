'''
dicio = {
    ('nome','anodelançamento') : ('Custodeprodução','diretor','atores') 
}       
'''

def existe(nomedicio):
    import os
    if os.path.exists(nomedicio):
        return True
    else:
        return False

def grava(nomedicio,dicio):
    refarq = open(nomedicio,'w')
    for valor,valor2 in dicio:
        custo,diretor,lista = dicio[valor,valor2]
        tup = ''
        for i in lista:
            tup += '\t' + i
        linha = valor + '\t'+ valor2 + '\t'+ custo +'\t'+ diretor + tup + '\n'
        refarq.write(linha)
    refarq.close()
    return 'Gravado!'

def le(nomedicio,dicio):
    if existe(nomedicio):
        refarq = open(nomedicio,'r')
        for linha in refarq:
            linha = linha[:len(linha)-1] # tiro o \n
            linha = linha.split('\t')
            lista = linha[4:]
            lis = []
            for valor in lista:
                lis.append(valor)
            dicio[(linha[0],linha[1])] = (linha[2],linha[3],lis)
        refarq.close()

def cria_filme(dicio):
    tup = ()
    nome = input('Nome do filme: ')
    ano = input('Ano de lançamento: ')
    if nome not in dicio:
        tup += (nome,ano)
        chave = ()
        custo = input('Custo de Produção: ')
        diretor = input('Diretor: ')
        esc = int(input('Numero de atores: '))
        lis = []
        for valor in range(0,esc):
            ator = str(input(f'Nome do ator {valor+1}: '))
            lis.append(ator)
        chave = (custo,diretor,lis)
        dicio[tup] = chave
        print(dicio[tup])
    else:
        return 'Filme já existe!'
    
def listar_todos(dicio):
    for valor,valor2 in dicio:
        print(valor,valor2,':',dicio[valor,valor2])

def listar_especifico(dicio):
    nome = input('Nome do filme: ')
    ano = input('Ano de lançament0: ')
    if (nome,ano) in dicio:
        print(nome,ano,':',dicio[(nome,ano)])
    else:
        return 'Filme não encontrado!'

def alterar(dicio):
    nome = input('Nome do filme: ')
    ano = input('Ano de lançament0: ')
    if (nome,ano) in dicio:
        Custodeprodução,diretor, atores = dicio[nome,ano] 
        esc_f = int(input('''O que deseja alterar?
                          1 - Custo de produção
                          2 - Diretor
                          3 - Atores
                          4 - Cancelar''')) 
        if esc_f == 1:
            Custo = input('Novo custo de produção: ')
            dicio[nome,ano] = Custo,diretor,atores
        elif esc_f == 2:
            dir = input('Novo Diretor: ')
            dicio[nome,ano] = Custodeprodução,dir,atores
        elif esc_f == 3:
            valor = int(input('Numero de atores que deseja colocar: '))
            tup = []
            for i in range(0,valor):
                tup.append(input(f'Ator {1+i}: '))
            dicio[nome,ano] = Custodeprodução,diretor,tup
        else:
            return print('Operação cancelada')
    else: return print('Não encontrado!')

def apague(dicio):
    nome = input('Nome do filme: ')
    ano = input('Ano de lançament0: ')
    if (nome,ano) in dicio:
        decisao= input(f'Certeza que deseja excluir {nome,ano,':',dicio[(nome,ano)]} digite 0 para confirmar ou 1 para cancelar: ')
        if decisao == '0':
            del dicio[(nome,ano)]
        else:
            return 'Operação cancelada!'
    else:
        return 'Não encontrado!'




