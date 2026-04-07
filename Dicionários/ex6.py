'''
6) Sistema para Gerenciamento de Carros:
Crie um programa que gerencie um dicionário com dados de CARROS.
A chave será a placa do carro (uma string).
O valor será uma lista, com os seguintes dados:
marca (string), modelo (string), lista com 2 inteiros: ano do carro, kilometragem rodada
'''
def existe(nomearq):                                           
    import os
    if os.path.exists(nomearq):
        return True
    else:
        return False
    
def grava(nomearq,dicio):                                             # D
    if len(dicio):
        refarq = open(nomearq,'w')
        for valor in dicio:
            marca,modelo,lista = dicio[valor]
            info = ''
            for i in lista:
                info += '\t' + str(i)
            linha = valor + '\t'+ marca + '\t' + modelo + info + '\n'
            refarq.write(linha)
        refarq.close()
        return 'Gravado!'
    else:
        return 'Dicionario não existe!'
    
def le(nomearq,dicio):                                                # E
    if existe(nomearq):
        refarq = open(nomearq,'r')
        for linha in refarq:
            linha = linha[:len(linha)-1]
            dados = linha.split('\t')
            # print(dados)
            dicio[dados[0]] = [dados[1],dados[2],[(int(dados[3])),(int(dados[4]))]]
        refarq.close()
    else:
        return 'dicionário não existe'

def novo_carro(dic):                                                   # A
    placa = input('Digita a Placa do novo veiculo: ')
    if placa not in dic:
        marca = input('Marca do veiculo: ')
        modelo = input('Modelo: ')
        ano = int(input('Ano: '))
        km = int(input('kilometragem: '))
        dic[placa] = [marca,modelo,[ano,km]]
        return 'Feito!'
    else:
        return 'placa já existe!'

def exibe(dicio):                                                      # B
    ac = 0
    for chave in dicio:
        marca,modelo,lista = dicio[chave]
        ac += lista[1]
        print(f'placa: {chave}, Marca: {marca}, Modelo: {modelo}, Ano: {lista[0]}, kms: {lista[1]}')
    print(ac,'Km total da garagem')

def carros_classicos(dicio):                                          # C
    f = False
    for chave in dicio:
        dic={}
        marca,modelo,lista = dicio[chave]
        if f == False:
            menor = lista[0]
            f = True
        if menor > lista[0]:
            menor = lista[0]
    
    for chave in dicio:
        marca,modelo,lista = dicio[chave]
        if lista[0] == menor:
            dic[chave] = marca,modelo,lista 
    print('\n')
    for valor in dic:
        marca,modelo,lista = dicio[valor]
        print(f'Marca: {marca}, Modelo: {modelo}, Ano: {lista[0]}, Kilometragem: {lista[1]}, placa: {valor}.')
    print('\n')


def menu():
    print('1 - Inserir carro')
    print('2 - Exibir todos os carros')
    print('3 - Exibir os carros mais velhos')
    print('4 - Ler dados de um arquivo')
    print('5 - Gravar dados em um arquivo')
    print('6 – FIM')

Exemplo = {
            'FDS1A11' : [ 'Jeep' ,'Renegade',[2022,1540]], #['datas de revisão'] fazer com esse dps
            'GYJ3J45' : [ 'Renault','Captur',[2023,325]],
            'QWS5Z32' : [ 'Hyunday','HB20',[2015,12320]],
            'FVT1I67' : ['honda','Titan',[2015,5000]]
            }

menu()
esc = int(input(""))
while esc != 6:
    if esc == 1:
        novo_carro(Exemplo)
    elif esc == 2:
        exibe(Exemplo)
    elif esc == 3:
        carros_classicos(Exemplo)
    elif esc == 4:
        nomearq = input('Nome do arquivo.txt')
        le(nomearq,Exemplo)
    elif esc == 5:
        nomearq = input('Nome do arquivo.txt')
        grava(nomearq,Exemplo)
    esc = int(input(""))
print('Obrigado! Fim do programa.')