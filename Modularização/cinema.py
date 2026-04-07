'''
Menu Principal:
1. Submenu de Salas
2. Submenu de Filmes
3. Submenu de Sessões
4. Submenu Consultas
5. Sair
'''
import filme
import sala
import sessao

def sub_menu():
    print('1 - listar todos')
    print('2 - listar específico')
    print('3 - incluir')
    print('4 - alterar')
    print('5 - excluir')
esc = int(input('''
Menu Principal:
1. Submenu de Salas
2. Submenu de Filmes
3. Submenu de Sessões
4. Submenu Consultas
5. Sair
escolha: '''))
while esc != 5:
    if esc == 1:
        dic_salas = {}
        # 1° carregar o arquivo de 'salas.txt' para o dic_salas
        sala.le('sala.txt',dic_salas)
        sub_menu()
        esc2 = int(input('Escolha: '))
        if esc2 == 1:
            sala.exibe_todas_salas(dic_salas)
        elif esc2 == 2:
            sala.exibe_espcifico(dic_salas)
        elif esc2 == 3:
            sala.cria_sala(dic_salas)
        elif esc2 == 4:
            sala.alterara(dic_salas)
        elif esc2 == 5:
            sala.excluir(dic_salas)
        sala.grava('Sala.txt',dic_salas)
        # chama sala.menu_sala(dic_salas)
        # salvar o dicionario dic_sala no arquivo 'salas.txt'
        sala.grava('sala.txt',dic_salas)
    elif esc == 2:
        dic_filmes = {}
        filme.le('filme.txt',dic_filmes)
        sub_menu()
        esc2 = int(input('Escolha: '))
        if esc2 == 1:
            filme.listar_todos(dic_filmes)
        elif esc2 == 2:
            filme.listar_especifico(dic_filmes)
        elif esc2 == 3:
            filme.cria_filme(dic_filmes)
        elif esc2 == 4:
            filme.alterar(dic_filmes)
        filme.grava('filme.txt',dic_filmes)   # ERRO NA HORA DE SALVAR
        #submenu filmes
    elif esc == 3:
        dic_sessoes ={}
        None
        #submenu sessões
    elif esc == 4:
        #submenu consultas
        None
    esc = int(input('''
        Menu Principal:
        1. Submenu de Salas
        2. Submenu de Filmes
        3. Submenu de Sessões
        4. Submenu Consultas
        5. Sair
        escolha: '''))
        