'''Utilizando dicionários, faça um programa que crie e leia um arquivo denominado
“Turma_ALG.txt”, para armazenar informações sobre as notas obtidas por cada aluno
de uma turma de Algoritmos em cada uma das 4 provas. Cada linha do arquivo terá o
nome de um aluno, o seu prontuário e a nota obtida pelo aluno em cada prova,
conforme no exemplo a seguir:

            Maria sc365987 6.5 4.0 7.5 5.0
            Roberto sc569874 4.5 3.0 6.0 5.0
            Carlos sc222222 7.0 8.0 9.0 10.0
            Pedro sc112141 9.0 6.0 10.0 7.0

O programa deverá implementar funções para:
a) Cadastrar um novo aluno com suas notas;
b) Calcular e apresentar a média (média aritmética das 4 provas) de cada
estudante;
c) Apresentar o nome e a média dos estudantes que obtiveram média menor
que 6.0;
d) Apresentar o nome e a média do estudante que obteve a menor média e a
maior média (se houver mais de um aluno, a função deverá exibir todos).'''
#=============================== Verifica se existe!
def exite_arq(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

dicio = {
    'Maria' : ('sc365987', [6.5, 4.0, 7.5, 5.0]),
    'Roberto' : ('sc569874', [4.5, 3.0,6.0, 5.0]),
    'Carlos' : ('sc222222', [7.0, 8.0, 9.0, 10.0]),
    'Pedro' : ('sc112141' ,[9.0, 6.0, 10.0, 7.0])
}

def cria_aluno(dicio):
    n = input('Nome do aluno que deseja cadastrar: ')
    if n not in dicio:
        ra = input('Ra: ')
        l_notas = []
        for valor in range(0,4):
            x = float(input(f'Nota {valor+1}: '))
            l_notas.append(x)
        dicio[n] = (ra,l_notas)





dic = {}
if exite_arq("Turma_ALG.txt"):
    ref_arq=open("Turma_ALG.txt",'r')
    for linha in ref_arq:
        linha = linha[:len(linha)-1]
        aluno = linha.split("\t")
        chave = aluno[0]
        ra = aluno[1]
        notas = aluno[2]
        dic[chave] = (ra,notas)
    ref_arq.close()
print(dic)


if len(dicio):
    ref_arq=open("Turma_ALG.txt",'w')
    for aluno in dicio:
        ra,notas=dicio[aluno] 
        a = str(notas)
        linha = aluno + '\t' + ra + '\t' + a + '\n'
        ref_arq.write(linha)
    ref_arq.close()
    print("Arquivo gravado!")