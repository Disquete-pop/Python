'''
Considere um arquivo texto (denominado “votos.txt”) que contém, em cada linha, o voto de
um eleitor, representado pelo código de identificação do candidato. Suponha que existam 5
candidatos, cujos códigos de identificação são: 100, 200, 300, 400, 500. Segue um exemplo
de arquivo:
 Faça um programa que leia o arquivo para apurar o resultado final da eleição. O programa
deverá implementar funções para:
 Calcular e apresentar a quantidade de votos por candidato;
 Calcular e apresentar a quantidade de votos do candidato mais votado;
 Calcular a quantidade de votos do candidato menos votado;
 Calcular e apresentar a quantidade de votos nulos (um voto nulo é um voto cujo código
de identificação é inválido).
Exercício 3
500
100
200
300
1555
0
...
Obs: as funções deverão retornar os resultados para serem impressos no programa principal.
Utilize parâmetros para fazer a transferência de dados entre as funções. NÃO USE VARIÁVEIS
GLOBAIS.
'''
# Verifica se existe o arquivo
def exite_arq(nomearq):
    import os
    if os.path.exists(nomearq):
        return True
    else:
        return False

# grava arquivo

def grava_arq(nomearq,dicio):
    if len(dicio):
        ref_arq = open(nomearq,'w')
        for eleitor in dicio:
            voto = dicio[eleitor]
            linha = eleitor + '\t' + voto + '\n'
            ref_arq.write(linha)
    ref_arq.close()
    return 'gravado com sucesso'

# lê o arquivo

def learq(nomearq):
    dicio2 = {}
    if exite_arq(nomearq):
        refarq = open(nomearq,'r')
        for linha in refarq:
            linha = linha[:len(linha)-1]
            dados = linha.split('\t')

            chave = dados[0]
            valor = dados[1]
            dicio2[chave] = valor
        refarq.close()
    return dicio2

dicio = {'1': '100',
        '2': '100',
        '3' : '200',
        '4' : '300',
        '5' : '500',
        '6' : '500',
        '7' : '300',
        '8' : '500',
        '9': '1234'
}
nomearq = ('votos.txt')
learq(nomearq)
print(grava_arq(nomearq,dicio))