'''
Sala  Dicionário de chave: INTEIRO e valor: TUPLA
Sala  Código: (Nome, Capacidade, TipoExibição, Acessível,complementos)

'''
def exitiste(nomearq):
    import os
    if os.path.exists(nomearq):
        return True
    else:
        return False

def grava(nomearq,dicio):
    if len(dicio):
        refarq = open(nomearq,'w')
        for chave in dicio:
            tup = dicio[chave]
            tupla = ''
            for valor in tup:
                tupla += '\t'+valor
            linha = str(chave) + tupla + '\n'
            refarq.write(linha)
        refarq.close()
        return 'Gravado!'

def le(nomearq,dicio):
    if exitiste(nomearq):
        refarq = open(nomearq,'r')
        for linha in refarq:
            linha = linha[:len(linha)-1] # tira o '\n'
            dados = linha.split('\t')
            chave = dados[0]
            tup = ()
            for valor in dados[1:]:
                tup += valor,
            dicio[int(chave)] = tup
        refarq.close

def cria_sala(dicio):
    esc1 = int(input('Numero de salas que deseja adicionar ou 0 para cancelar '))
    if esc1 > 0:
        while esc1 != 0:
            chave = int(input('Número da sala ou 0 para cancelar: '))
            if chave not in dicio:
                if chave == 0:
                    esc1 = 0
                    return print( 'Operação cancelada!')
                else:
                    finalizador = 1
                    while finalizador == 1:
                        tup = ()
                        nome = input('Nome: ')
                        capacidade = input('Capacidade: ')
                        tip = input('Tipo de exibição: ')
                        ac = input('Acessível: ')
                        info = int(input('Deseja colocar mais infomrações? digite o numero de itens ou 0 para não colocar. '))
                        tup += (nome,capacidade,tip,ac,)
                        if info > 0:
                            for valor in range(info):
                                informacao = input('Informação adicional: ')
                                tup += (informacao,)
                        finalizador = 0
                dicio[chave] = tup
                esc1 -= 1
            else:
               return print('Sala já existe!')
    if esc1 == 0:
        print( 'Operação cancelada!')
    
def exibe_todas_salas(dicio):
    for valor in dicio:
        print('Sala:',valor,'\n')
        for i in dicio[valor]:
            
            print(i,end=' ')
        print('\n')

def exibe_espcifico(dicio):
    chave = int(input('Numero da Sala: '))
    if chave in dicio:
        print(f'chave',':',dicio[chave])

def alterara(dicio):
    sala = int(input('Numero da sala que deseja alterar: '))
    if sala in dicio:
        tup = ()
        nome = input('Nome: ')
        capacidade = input('Capacidade: ')
        tip = input('Tipo de exibição: ')
        ac = input('Acessível: ')
        info = int(input('Deseja colocar mais infomrações? digite o numero de itens ou 0 para não colocar. '))
        tup += (nome,capacidade,tip,ac,)
        if info > 0:
            for valor in range(info):
                informacao = input('Informação adicional: ')
                tup += (informacao,)
        finalizador = 0
        dicio[sala] = tup
    else:
        return 'Sala não encontrada'

def excluir(dicio):
    sala = int(input('Numero da sala que deseja excluir: '))
    if sala in dicio:
        print(sala,':',dicio[sala])
        confirmacao = input('Deseja excluir essa sala? digite 0 para confirmar ou Enter para cancelar.')
        print('\n')
        if confirmacao == '0':
            del dicio[sala]
    else:
        return 'sala não encontrada.'
    
