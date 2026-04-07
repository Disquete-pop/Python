'''
Implemente um sistema de gerenciamento de contatos de
prestadores de serviços, cuja chave deve ser o e-mail
pessoal. As informações adicionais do contato devem estar
em uma lista: nome, data de nascimento e uma lista de
tuplas, onde cada tupla deve conter a especialidade
(encanador, mecânico etc) e valor da hora. O menu do 
sistema deve ofereser as seguintes opções

=====================================================

As informações adicionais do contato devem estar
em uma lista: nome, data de nascimento e uma lista de
tuplas, onde cada tupla deve conter a especialidade
(encanador, mecânico etc) e valor da hora

=====================================================

1 adc. contato
2 exibir contato
3 excluir contato
4 alterar contato
5 sair

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
        lista = []
        
        contato = str(input('Email: '))
        if contato != '':
            while len(lista) <= 2:
                if len(lista) == 0:
                    lista.append(str(input('Nome: ')))
                elif len(lista) == 1:
                    dia = str(input('Digite o dia com dois digitos ex 01: '))
                    if int(dia) < 32 and len(dia) == 2:
                        mes = str(input('Mes com dois digitos ex 01-12: '))
                        if int(mes) <=12 and len(mes) ==2:
                            ano = str(input('Ano: '))
                            if int(ano) <= 2025 and len(str(ano)) == 4:
                               data = (f'{dia}/{mes}/{ano}')
                               lista.append(data)
                            else:
                                print('ano invalido')
            
                        else:
                            print('mes invalido')
                          
                    else:
                        print('Dia invalido')
            
                elif len(lista) == 2:
                    x = input('Ocupação: ')
                    l2 = []

                    while x != '0':
                        tup = ()
                        tup += (x,)
                        y = int(input('Valor da hora: '))
                        tup += (f'R$: {y}',)
                        l2.append(tup)
                        x = input('Digite outra ocupação ou 0 para cancelar: ')
                    lista.append(l2)
                    dicio[contato] = lista
        print(dicio)
        print(end='\n')
    if escolha == 2:
        for valor in dicio:
            print(valor, ':',dicio[valor] )
        print(end='\n')
    if escolha == 3:
        print(end=' ')
        excluir = input('Email: ')
        if excluir in dicio:
            del dicio[excluir]
            print('feito!')
        else:
            print('Contato invalido!')
        print(end='\n')
    if escolha == 4:
        x = input('Email do contato que deseja alterar: ')
        if x in dicio:
            print("Contato existe!")
        else:
            print("Contato não encontrado.")
        print(end='\n')
        for valor in dicio:
            if valor == x:
                lista = []
                while len(lista) <= 2:
                    if len(lista) == 0:
                        lista.append(str(input('Nome: ')))
                    elif len(lista) == 1:
                        lista.append(str(input('Data de nascimento, ex aa/bb/cccc: ')))
                    elif len(lista) == 2:
                        x = input('Ocupação: ')
                        l2 = []
                        while x != '0':
                            tup = ()
                            tup += (x,)
                            y = int(input('Valor da hora: '))
                            tup += (f'R$: {y}',)
                            l2.append(tup)
                            x = input('Digite outra ocupação ou 0 para cancelar: ')
                        lista.append(l2)
                        dicio[valor] = lista
            print(dicio)
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

'''
como modificar o email
evitar repetições
verificação da data
'''