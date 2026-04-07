'''
exercicio de dicionarios e tuplas
dic_alunos[(RA, nome)] = (data_nasc,[e-mails],[telefones])

'''
dicio = {}
escolha = int(input('''
=====================================
1 adc. contato
2 exibir contato
3 excluir contato
4 alterar contato
5 sair
=====================================
Escolha : '''))
while 0 < escolha <= 4:
    if escolha == 1:
    # chave com a tupla
        tup = ()
        tup2 = ()
        passos = 0
        contato = str(input('sigla do RA: ')).upper()
        corretor = 0
        num_1 = ''
        verificador = '0123456789'
        while corretor < 7:
            num = str(input(f"digito {corretor+1} do RA:"))
            if num in verificador:
                num_1 += num
                corretor += 1
            else:
                print('Valor invalido, digite um numero!')
        ra = contato + num_1
        nome = str(input('Nome: '))
        tup += (ra,nome,)
        print(tup)
        if nome != '':
            while passos != 3:
                if passos == 1:
                    lista_email = []
                    flag = False
                    while flag != True:
                        email = (str(input('Email ou enter para continuar: ')))
                        if email == '' and len(lista_email) != 0:
                            flag = True
                        else:
                            lista_email.append(email)
                    tup2 += (lista_email,)
                    print(tup2)
                    passos += 1
                elif passos == 0:
                    dia = str(input('Digite o dia com dois digitos ex 01: '))
                    if int(dia) < 32 and len(dia) == 2:
                        mes = str(input('Mes com dois digitos ex 01-12: '))
                        if int(mes) <=12 and len(mes) ==2:
                            ano = str(input('Ano: '))
                            if int(ano) <= 2025 and len(str(ano)) == 4:
                               data = (f'{dia}/{mes}/{ano}')
                               tup2 += (data,)
                               passos += 1
                               print(tup2)
                            else:
                                print('ano invalido')
            
                        else:
                            print('mes invalido')
                          
                    else:
                        print('Dia invalido')
            
                elif passos == 2:
                    lista_telefones = []
                    flag = True
                    while flag != False:
                        tel = str(input('Telefones ou digite enter para cancelar: '))
                        if tel == '' and len(lista_telefones) != 0:
                            flag = False
                        else:
                            lista_telefones.append(tel)
                    tup2 += (lista_telefones,)
                    dicio[tup] = tup2
                    passos += 1
                    for valor in dicio:
                        print(valor, ':',dicio[valor])
                print(end='\n')
    if escolha == 2:
        for valor in dicio:
            print(valor, ':',dicio[valor] )
        print(end='\n')
    if escolha == 4:
        print(end=' ')
        excluir = input('RA ou Nome: ')
        a = 0
        print(end='\n')
        while a != 1:
            certeza = input(f'Certeza que deseja alterar o contato {excluir}? Digite Sim para ou Não:').upper()
            if certeza in ['SIM','NÃO','NAO']:
                a += 1
                print(end='\n')
            else:
                print('Digite um valor valido! ')
                print(end='\n')
        if certeza == 'SIM':
            confir_chave = False
            achado = False
            for ra_,nome_ in dicio:
                # jeito mais manual
                valor = dicio[(ra_, nome_)]
                data_ = valor[0]
                emails_ = valor[1]
                telefones_ = valor[2]
             #  data, emails, telefones = dicio[(ra_, nome_)] jeito alternativo 
             # # atribuimos esse valores a chave. que recebem os valor dentro dela
                if ra_ == excluir or nome_ == excluir:
                    achado = True                                   # como a chave é uma tupla de 2 itens, pode-se usar isso mostra um, dps o outro.
                                                                    # se fosse chave in dicio: ele mostraria (chave 1, chave 2,)
                    print('O que deseja alterar?')
                    print('1 - Adicionar novo email')
                    print('2 - Adicionar novo telefone')
                    print('3 - Alterar data de nascimento')
                    print('4 - Para cancelar!')
                    escolha_ = input('Escolha: ')
                    if escolha_ == '1':
                        novo_email_ = input('Digite o novo email: ')
                        emails_.append(novo_email_)
                        dicio[(ra_,nome_)] = (data_,emails_,telefones_)
                        print('feito!')
                    elif escolha_ == '2':
                        novo_telefone_ = input('Novo telefone: ')
                        telefones_.append(novo_telefone_)
                        dicio[(ra_, nome_)] = (data_,emails_,telefones_)
                        print('feito!')
                    elif escolha_ =='3':
                        validador = 0
                        while validador != 3:
                            if validador == 0:
                                dia = str(input('Digite o dia com dois digitos ex 01: '))
                                if int(dia) < 32 and len(dia) == 2:
                                    validador += 1
                                else:
                                            print('ano invalido')
                            if validador == 1:   
                                mes = str(input('Mes com dois digitos ex 01-12: '))
                                if int(mes) <=12 and len(mes) ==2:
                                    validador += 1
                                else:
                                        print('mes invalido')
                            if validador == 2:
                                ano = str(input('Ano: '))
                                if int(ano) <= 2025 and len(str(ano)) == 4:
                                    nova_data_ = (f'{dia}/{mes}/{ano}')
                                    dicio[(ra_,nome_)] = (nova_data_,emails_,telefones_)
                                    print('feito!')
                                    validador += 1
                                else:
                                    print('ano invalido')  
                    elif escolha_ == '4':
                        achado = True
                        print('Operação cancelada!')
        if achado == False and certeza not in ['NÃO','NAO']:
            print('contato invalido!')
        print(end='\n')
    if escolha == 3:
        confirma_1 = input('RA ou Nome: ')
        achado = False
        modificado = False
        for chave1,chave2 in dicio:
            if chave1 == confirma_1 or chave2 == confirma_1:
                print('Contato localizado! ')
                achado = True
                value = 0
                while value != 1:
                    confirma_2 = input('Digite 1 para confirmar ou 0 para cancelar: ')
                    if confirma_2 == '1':
                        guardador_para_excluir = (chave1,chave2)
                        modificado = True
                        value += 1
                    elif confirma_2 == '0':
                        value += 1
                    else:
                        print('insira um valor valido!')
        if achado == False:
            print('contato invalido')
        if modificado == True:
            print('Operação relizada com sucesso!')
            del dicio[guardador_para_excluir]
        if achado == True and modificado == False:
            print('Operação cancelada com sucesso!')
        print(end='\n')
    escolha = int(input('''
=====================================
1 adc. contato
2 exibir contato
3 excluir contato
4 alterar contato
5 sair
=====================================
Escolha : '''))
if escolha == 5:
        print(end='\n')
        print('Fim do programa! :)')
        print(end='\n')
