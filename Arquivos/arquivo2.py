def escolha_():
        print("Notas dos alunos:\n")
        print("1 - Cadastrar um novo aluno com suas notas")
        print("2 - Calcular e apresentar a média")
        print("3 -  Apresentar o nome e a média dos estudantes que obtiveram média menor que 6.0")
        print("4 -  Apresentar o nome e a média do estudante que obteve a menor média e a maior média")
        print("5 - Sair")

#=========================
def exist_arq_(nomearq):
        import os
        if os.path.exists(nomearq):
                return True
        else:
                return False
#=========================

# Lê o arquivo

def le_arquivo_(dc,nomearq):
    if exist_arq_(nomearq):
        ref_arq = open(nomearq,'r')
        for linha in ref_arq:
            linha = linha[:len(linha)-1]          # tira o \n
            aluno = linha.split('\t')             # tira os \t
            chave = aluno[0]
            ra = aluno[1]
            notas = [float(aluno[2]),float(aluno[3]),float(aluno[4]),float(aluno[5])]
            dc[chave] = (ra,notas)
        ref_arq.close()

# Grava ele / atualiza

def grava_arq_(dc,nomearq):
    if len(dc):
        ref_arq = open(nomearq,"w")
        for aluno in dc:
            ra,notas = dc[aluno]
            linha = aluno + '\t' + ra + '\t' + str(notas[0]) +'\t' + str(notas[1]) +'\t' + str(notas[2]) +'\t' + str(notas[3]) +'\n'
            ref_arq.write(linha)
        ref_arq.close()
        print('Arquivo salvo')

# cadastra um novo aluno

def cria_aluno_(dicio):
    n = input('Nome do aluno que deseja cadastrar: ')
    if n not in dicio:
        ra = input('Ra: ')
        l_notas = []
        for valor in range(0,4):
            x = float(input(f'Nota {valor+1}: '))
            l_notas.append(x)
        dicio[n] = (ra,l_notas)
    else:
        input('Nome já exite! Aperte enter para continuar... ')

# Media
def Med_(dc):
    print("\nMÉDIAS DOS ALUNOS:")
    for nome in dc:
        ra,notas = dc[nome]
        media = 0
        for i in notas:
            media += i
        media_ = media / 4
        print(f'A media de {nome} é: {media_}')

# media < 6
def Med_abaixo(dc):
    for nome in dc:
        ra,notas=dc[nome]
        media = 0
        for i in notas:
            media += i
        media = media / 4
        if media < 6:
            print(f'A media de {nome} é: {media}')

def menor_med(dc):
    f = 1
    menor_media = 0
    nome_ = ''
    for nome in dc:
        ra,notas = dc[nome]
        media = 0
        for i in notas:
            media += i
        media = media /4
        if f == 1:
            menor_media = media
            nome_ = nome
            f = 0
        elif media < menor_media:
            menor_media = media 
            nome_ = nome
    print(f'A menor media é de {nome_} é {menor_media}')
nomearq = "Turma_ALG.txt"
esc = 0
dicio = {
    'Maria' : ('sc365987', [6.5, 4.0, 7.5, 5.0]),
    'Roberto' : ('sc569874', [4.5, 3.0,6.0, 5.0]),
    'Carlos' : ('sc222222', [7.0, 8.0, 9.0, 10.0]),
    'Pedro' : ('sc112141' ,[9.0, 6.0, 10.0, 7.0])
}
le_arquivo_(dicio,nomearq)
while esc != 6:
    escolha_()
    esc = int(input('Escolha: '))
    if esc == 1:
        cria_aluno_(dicio)
    elif esc == 2:
        Med_(dicio)
    elif esc == 3:
        Med_abaixo(dicio)
    elif esc == 4:
        menor_med(dicio)
    elif esc == 5:
        grava_arq_(dicio,nomearq)
        esc = 6