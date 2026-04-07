def Existe_Arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False
    
dicio = {'SC132': ('aluno 1','email.aluno1A@ifsp'),
         'SC133': ('aluno 2','email.aluno2A@ifsp'),
         'SC134': ('aluno 3','email.aluno3A@ifsp')
         }

dic = {}
if Existe_Arquivo("cad_alunos.txt"):
    ref_arq=open("cad_alunos.txt",'r')
    for linha in ref_arq:
        linha = linha[:len(linha)-1]
        aluno = linha.split("\t")
        chave = aluno[0]
        nome = aluno[1]
        email = aluno[2]
        dic[chave] = (nome,email)
    ref_arq.close()
print(dic)

dic2 = {}
if Existe_Arquivo("cad_alunos.txt"):
    ref_arq=open("cad_alunos.txt",'r')
    linha=ref_arq.readline()
    while linha != '':
        linha = linha[:len(linha)-1]
        aluno = linha.split("\t")
        chave = aluno[0]
        nome = aluno[1]
        email = aluno[2]
        dic2[chave] = (nome,email)
        linha = ref_arq.readline()
    ref_arq.close()
print(dic2)

if len(dicio):
    ref_arq=open("cad_alunos.txt",'w')
    for aluno in dicio:
        ra = aluno
        nome,email = dicio[ra]
        linha = ra + '\t' + nome + '\t' + email + '\n'
        ref_arq.write(linha)
    ref_arq.close()
    print('Arquivo gravado com sucesso')

