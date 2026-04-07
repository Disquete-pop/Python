def exist_arq(nomearq):
    import os
    if os.path.exists(nomearq):
        return True
    else:
        return False


def le_arquivo(dc, nomearq):
    if exist_arq(nomearq):
        ref_arq = open(nomearq, 'r')
        for linha in ref_arq:
            linha = linha[:len(linha)-1]  # remove o \n do final
            aluno = linha.split('\t')     # separa por TAB
            nome = aluno[0]
            ra = aluno[1]
            notas = [float(aluno[2]), float(aluno[3]), float(aluno[4]), float(aluno[5])]
            dc[nome] = (ra, notas)
        ref_arq.close()


def grava_arquivo(dc, nomearq):
    if len(dc):
        ref_arq = open(nomearq, 'w')
        for nome in dc:
            ra, notas = dc[nome]
            linha = nome + '\t' + ra + '\t' + str(notas[0]) + '\t' + str(notas[1]) + '\t' + str(notas[2]) + '\t' + str(notas[3]) + '\n'
            ref_arq.write(linha)
        ref_arq.close()
        print("Arquivo gravado com sucesso!")


def cadastra_aluno(dc):
    print("\nCadastrar novo aluno:\n")
    nome = input("Nome do aluno: ")
    ra = input("RA: ")
    notas = []
    for i in range(1, 5):
        nota = float(input(f"Nota {i}: "))
        notas.append(nota)
    dc[nome] = (ra, notas)


def mostra_medias(dc):
    print("\nMÉDIAS DOS ALUNOS:")
    for nome in dc:
        ra, notas = dc[nome]
        media = sum(notas) / 4
        print(f"{nome} ({ra}) -> Média: {media:.2f}")


def menores_que_seis(dc):
    print("\nALUNOS COM MÉDIA < 6.0:")
    for nome in dc:
        ra, notas = dc[nome]
        media = sum(notas) / 4
        if media < 6.0:
            print(f"{nome} ({ra}) -> Média: {media:.2f}")


def maior_menor_media(dc):
    if len(dc) == 0:
        print("Nenhum aluno cadastrado.")
        return

    medias = {}
    for nome in dc:
        ra, notas = dc[nome]
        medias[nome] = sum(notas) / 4

    menor = min(medias.values())
    maior = max(medias.values())

    print("\nAluno(s) com MENOR média:")
    for nome in medias:
        if medias[nome] == menor:
            print(f"{nome} -> Média: {menor:.2f}")

    print("\nAluno(s) com MAIOR média:")
    for nome in medias:
        if medias[nome] == maior:
            print(f"{nome} -> Média: {maior:.2f}")


# ===================== Programa Principal =====================
dicio = {}
nomearq = "Turma_ALG.txt"

le_arquivo(dicio, nomearq)

opcao = 0
while opcao != 5:
    print("\n1 - Cadastrar aluno")
    print("2 - Mostrar médias")
    print("3 - Mostrar alunos com média < 6.0")
    print("4 - Mostrar aluno(s) com maior e menor média")
    print("5 - Sair e salvar")
    opcao = int(input("Opção: "))

    if opcao == 1:
        cadastra_aluno(dicio)
    elif opcao == 2:
        mostra_medias(dicio)
    elif opcao == 3:
        menores_que_seis(dicio)
    elif opcao == 4:
        maior_menor_media(dicio)
    elif opcao == 5:
        grava_arquivo(dicio, nomearq)
        print("Encerrando...")
