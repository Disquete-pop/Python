'''
nomefilme,anolancamento,codsala,data,horario : preço do infgresso
    print('1 - listar todos')
    print('2 - listar específico')
    print('3 - incluir')
    print('4 - alterar')
    print('5 - excluir')

'''

def existe(nomedicio):
    import os
    if os.path.exists(nomedicio):
        return True
    else :
        return False
    
def grava(nomedicio,dicio):
    if len(dicio):
        refarq = open(nomedicio,'w')
        for nome,ano,cod,data,hora in dicio:
            valor = dicio[nome,ano,cod,data,hora]
            linha = nome + '\t' + ano + '\t'+ cod + '\t'+ data + '\t' + hora + '\t' + valor
            refarq.write(linha)
        refarq.close
        return print('Gravado')

def le(nomedicio,dicio):
    if existe(nomedicio):
        refarq = open(nomedicio,'r')
        for linha in refarq:
            linha = linha[:len(linha)-1]
            dados = linha.split('\t')
            nome = dados[0]
            ano = dados[1]
            cod = dados[2]
            data = dados[3]
            hora = dados[4]
            chave = dados[5]
            dicio[(nome,ano,cod,data,hora)] = chave
        refarq.close()

def listar_todos(dicio):
    for nome,ano,cod,data,hora in dicio:
        print(nome,ano,cod,data,hora,':',dicio[nome,ano,cod,data,hora])

def lista_especifico(dicio):
    cod = input('código da sala: ')
    achou = False
    for valor in dicio:
        nome,ano,codsala,data,hora=valor                                     # digitar tudo ou dar a opção de só o codigo da sala
        if codsala == cod:
            print(nome,ano,cod,data,hora,':',dicio[nome,ano,cod,data,hora])     
            achou = True
    if not achou:
        return print('codigo invalido')

def incluir(dicio):
    nome = input('Nome do filme: ')
    ano = input('Ano de lançamento: ')
    cod = input('Codigo da sala: ')
    data = input('Data: ')
    hora = input('Hora: ')
    if [nome,ano,cod,data,hora] not in dicio[(nome,ano,cod,data,hora)]:
        dicio[nome,ano,cod,data,hora] = input('Preço: ')
    else:
        return 'Já existe'
    
