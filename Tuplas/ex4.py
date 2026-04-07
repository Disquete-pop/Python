def incluirNovoNome(dicio):
    nome = input('Nome do contato que deseja colocar: ')
    if nome not in dicio:
        numero = int(input('Numero: '))
        dicio[nome] = [numero]
        valor = input('Deseja adicionar mais um numero? S/N ').upper()
        if valor == 'S':
                while valor != 'N':
                    numero = int(input('Numero: '))
                    dicio[nome].append(numero)
                    valor = input('Deseja adicionar mais um numero? S/N ').upper()
                if valor == 'N':
                    print(nome,":",dicio[nome])
                    return 
        elif valor != ['N','S']:
            print('Valor invalido.')

                
    else:
        print('Contato já existe :( ')
        return dicio
            
def incluirTelefone(dicio):
     if escolha == 2:
        nome = str(input('Nome do contato que deseja adicionar um numero: '))
        for valor in dicio:
            if valor == nome:
                dicio[valor].append(int(input('Numero que deseja adicionar: ')))
        if nome not in dicio:
            esc = str(input('Contato não encontrado, deseja adicionar na agenda? s/n ')).upper()
            if esc == 'S':
                return incluirNovoNome(dicio)
            elif esc == 'N':
                return 'Operação cancelada'
            else:
                return 'Valor invalido'

def excluirTelefone(dicio):
    nome = str(input('Nome que deseja excluir: '))
    for valor_ in dicio:
            if valor_ == nome:
                print('Contato encontrador!')
                print(dicio[valor_])
                cont = 1
                for valor in dicio[valor_]:
                    res = dicio[valor_]
                    print(cont,' ',valor)
                    cont += 1
                esc = int(input('Escolha um contato para apagar: '))
    if len(res) > 0:
        del res[esc-1] 
    if len(dicio[nome]) == 0:
        del dicio[nome]

def excluirNome(dicio):
    nome = str(input('Nome que deseja excluir: '))
    if nome in dicio:
        for valor in dicio:
            if valor == nome:
                nome_ = valor
        del dicio[nome_]
    else:
        return 'Não encontrado! '

def consultaTelefone(dicio):
    nome = str(input('Nome que deseja buscar: '))
    if nome in dicio:
        for valor in dicio:
            if valor == nome:
                return nome, dicio[nome]
    else:
        return 'Nome não encontrado'

dicio = {'coiso' : [1000,1111],
         'Abobora' : [2000,2222]}

print('''
========= AGENDA TELEFÔNICA =========
1 - Incluir novo nome
2 - Incluir telefone
3 - Excluir telefone
4 - Excluir nome
5 - Consultar um telefone
6 - Consultar todos os telefones
7 - Para sair
=====================================
''')

escolha = int(input('Escolha: '))
while escolha <= 6:
    if escolha == 1:
        print(incluirNovoNome(dicio))
    elif escolha == 2:
        print(incluirTelefone(dicio))
    elif escolha == 3:
        print(excluirTelefone(dicio))
    elif escolha == 4:
        print(excluirNome(dicio))
    elif escolha == 5:
        print(consultaTelefone(dicio))
    if escolha == 6:
        for valor in dicio:
            print(valor, ':', dicio[valor])
        if len(dicio) == 0:
            print('Agenda vazia :( ')
    escolha = int(input('''
========= AGENDA TELEFÔNICA =========
1 - Incluir novo nome
2 - Incluir telefone
3 - Excluir telefone
4 - Excluir nome
5 - Consultar um telefone
6 - Consultar todos os telefones
7 - Para sair
=====================================
Escolha: '''))
if escolha > 7:
    print('Valor invalido!')
print('\n')
print('Fim do programa :) ')
print('\n')