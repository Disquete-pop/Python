# Faça um programa em Python que inicie com as duas estruturas de dados vazias e fique em execução até
# o usuário escolher a opção “Finalizar o programa” do seguinte menu:
# 1. Cadastrar um novo aluno sem repeƟção de nome
# 2. Consultar a idade de um aluno a parƟr de seu nome
# 3. Alterar a idade de um aluno a parƟr de seu nome
# 4. Remover um aluno a parƟr de seu nome
# 5. Cadastrar a nota de uma prova de uma disciplina para um aluno a parƟr de seu nome
# 6. Consultar todas as notas de provas de todas as disciplinas de um aluno a parƟr de seu nome
# 7. Alterar a nota de uma prova de uma disciplina para um aluno a parƟr de seu nome/disciplina/prova
# 8. Remover uma prova de uma disciplina com sua respecƟva nota de um aluno a parƟr de seu
# nome/disciplina/prova
# 9. Finalizar o programa
escolha = input('1 a 9 ou finalizar o programa ')
alunos=[ ['João Pedro Souza', 18], ['Isabela Moraes', 17], ['Daniel Silva', 19] ]
notas=[ [['MAT', 'P1', 5.8], ['ALG', 'P1', 7.4], ['WEB', 'P1', 8.9], ['ALG', 'P2', 9.6]], 
      [ ['ALG', 'P1', 9.2], ['WEB', 'P1', 6.7], ['WEB', 'P2', 9.3] ],
      [ ['MAT', 'P1', 5.8], ['ALG', 'P1', 9.6], ['MAT', 'P2', 8.1], ['MAT', 'P3', 8.1]]]
x = ''
i = 0
f = True
# 1
if escolha == '1':
    print('Para sair digite Sair')
    while x != True:
        x = input('Nome do aluno: ')
        n = False
        if x == 'Sair':
            n = True
            x = True
        for v in alunos:
            if x == v[0]:
                n = True
                print('Nome já existente')
        if n == False:
            i = int(input('Idade: '))
            alunos.append([x,i])
    print(alunos)
# 2
if escolha == '2':
    print(alunos)
    print('Escreva o Nome do aluno que deseja buscar a nota: ')
    x = input()
    if x != 'Sair':
        for a in alunos:
            if a[0] == x:
                print(a[1])
# 3
if escolha == '3':
    print(alunos)
    print('Escreva o Nome do aluno que deseja buscar a nota: ')
    x = input()
    if x != 'Sair':
        for a in alunos:
            if a[0] == x:
                a[1] = int(input('Nova idade: '))
        print(alunos)
# 4
if escolha == '4':
    print(alunos)
    x = input('Escreva o Nome do aluno que deseja buscar remover: ')
    if x != 'Sair':
        nova_lista = []
        for a in alunos:
            # if a[0] != x:
            #     del a[0]
            #     del a[0]
            # print(alunos)
            if a[0] != x:
                nova_lista.append(a)
        alunos = nova_lista
        print(alunos)
# 5
if escolha == '5':
    x = input('Escreva o Nome: ')
    if x!= 'Sair':
        for i in alunos:
            if i == alunos[0]:
                a # terminar dps