def mostra_menu():
    print("\n\nAgenda de Contatos:\n")
    print("1 - Adicionar Contato")
    print("2 - Exibir Contato")
    print("3 - Excluir Contato")
    print("4 - Alterar Contato")
    print("5 - Sair")

#=====================================================================
def Existe_Arquivo(nomearq):
    import os
    if os.path.exists(nomearq):
        return True
    else:
        return False

#=====================================================================
def le_arquivo_contato(dc, nomearq):

    if Existe_Arquivo(nomearq):
        ref_arq=open(nomearq,'r')
        linha=ref_arq.readline()
        while linha != '':
            #retira o \n e o *
            linha=linha[:len(linha)-2]
            contato = linha.split("#")
            email=contato[0]
            nome=contato[1]
            datanasc=contato[2]
            especialidades=contato[3].split("*")
            #quebrar cada item da lista de especialidades em & para montar a tupla
            indice=0
            for item in especialidades:
                t=item.split('&')
                tupla=(t[0], float(t[1]))
                especialidades[indice]=tupla
                indice+=1
            dc[email]=[nome, datanasc, especialidades]
            linha=ref_arq.readline()
        ref_arq.close()


#=====================================================================
def grava_arquivo_contato(dc, nomearq):
    if len(dc):
        ref_arq=open(nomearq,'w')
        for contato in dc:
            email=contato
            nome, datanasc, especialidades = dc[contato]
            linha = email + "#" + nome + "#" + datanasc + "#"
            for tupla in especialidades:
                esp=tupla[0]
                hora=tupla[1]
                linha=linha + esp+ "&" + str(hora) + "*"
            linha=linha + "\n"
            ref_arq.write(linha)
        ref_arq.close()
        print("Arquivo gravado com sucesso!")


#=====================================================================
def existe_contato(dc, email):
    if email in dc:
        return True
    else:
        return False
    
#=====================================================================

def insere_contato(dc):
    print("\nNovo contato\n")
    email=input('E-mail do contato: ')
    if existe_contato(dc, email):
        print("Contato já cadastrado!!!")
    else:
        dados=[]
        nome=input('Nome: ')
        dt=input('Data de nascimento (DD/MM/AAAA): ')
        n=int(input('Quantidade de especialidades: '))
        especialidades=[]
        for i in range(n):
            esp=input(f'Especialidade {i+1}: ')
            v_hora=float(input('Valor da hora: '))
            tupla=(esp, v_hora)
            especialidades.append(tupla)
        dados.append(nome)
        dados.append(dt)
        dados.append(especialidades)
        #insere no dicionario
        dc[email]=dados

#=====================================================================
def mostra_contato(dados):
        # mostra os dados formatados
        print(f'Nome: {dados[0]}')
        print(f'Data de Nascimento: {dados[1]}')
        print(f'Especialidades:')
        for item in dados[2]:
            print(f'{item[0]} - Valor da hora: {item[1]}')
            
#=====================================================================

def exibe_contato(dc, email):

    if existe_contato(dc, email):
        info=dc[email]
        mostra_contato(info)
    else:
        print("Contato não cadastrado!!!")
    input("Aperte qualquer tecla para continuar...")

#=====================================================================
def exclui_contato(dc, email):    

    if existe_contato(dc, email):
        info=dc[email]
        mostra_contato(info)
        opc=input("\nConfirma a exclusão do contato (S/N)?")
        if opc.upper() == 'S':
          del dc[email]
          print("Contato removido com sucesso!!!")
    else:
        print("Contato não cadastrado!!!")
    input("Aperte qualquer tecla para continuar...")
    
#=====================================================================
       
def altera_contato(dc, email):    
    print("\nAlterar contato")

    if existe_contato(dc, email):
        info=dc[email]
        mostra_contato(info)
        # pergunte o que ela deseja alterar e altere somente um item por vez
        print("Contato alterado com sucesso!!!")
    input("Aperte qualquer tecla para continuar...")
             
       
#============Programa Principal=========================================
            

dic_contatos={}
#carrega os dados do arquivo, se existirem
le_arquivo_contato(dic_contatos, "contatos.txt")
print(dic_contatos)
opc=0
while opc != '5':
    mostra_menu()
    opc=input("\nEscolha uma opção: ")
    if opc == '1':
        insere_contato(dic_contatos)
        print(dic_contatos)
    elif opc == '2':
        contato=input("Digite o e-mail do contato: ")
        exibe_contato(dic_contatos, contato)
    elif opc == '3':
        contato=input("Digite o e-mail do contato: ")
        exclui_contato(dic_contatos, contato)
    elif opc == '4':
        contato=input("Digite o e-mail do contato: ")
        altera_contato(dic_contatos, contato)
#grava os dados existentes no arquivo
grava_arquivo_contato(dic_contatos, "contatos.txt")    
print('\n--- Fim do Programa ---')  