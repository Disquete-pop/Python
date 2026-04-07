# # ex 8 da lista 1
# def meses(data):
#     escrito = ''
#     mes= ['01Janeiro','02Fevereiro','03Março','04Abril','05Maio','06Junho','07Julho','08Agosto','09Setembro','10Outubro','11Novembro','12Dezembro']

#     for i in mes:
#         if i[:2] == data[3:5]:
#             escrito = i[2:]
#     return print(f'{data[0:2]} {escrito} {data[6:]}')

# x = input('Coloque a data ex: aa/bb/cccc ')
# y = meses(x)

# ex 9
# def numero(x):
#     num = x
#     y = ''
#     menorq10 = ['zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove']
#     maiorq10menorq20 = ['Dez','onze','douze','treze','quatorze','quinze','dezeseis','desesete','dezoito','dezenove',]
#     maiorq20 = ['','vinte','vinte e ','trinta e ','quarenta e ','cinquienta e ','sessenta e ','setenta e ','oitenta e ','noventa e ']
#     if num < 10:
#         print(menorq10[num])
#     elif 10 < num < 20:
#         valor = num % 10
#         y = maiorq10menorq20[valor]
#     elif num >= 20:
#         if num == 20:
#             y = maiorq20[1]
#         else:
#             primeiro = num // 10
#             segundo = num % 10
#             y = maiorq20[primeiro] + menorq10[segundo]
#     elif num > 99:
#         y = 'Valor invalido'
#     return y

# Valor = int(input('Numero de 0 a 99: '))
# print(numero(Valor))

# # Ex 20
# def Anagrama(frase1,frase2):
#     a = []
#     b = []
#     ana = True
#     if len(frase1) > len(frase2):
#         return print('Não é um anagrama')
#     for i in frase1:
#         a.append(i)
#     for j in frase2:
#         b.append(j)
#     for k in range(len(a)):
#         for l in range(len(b)):
#             if a[k] == b[l]:
#                 a[k] = ''
#                 b[l] = ''
#     print(a)
#     print(b)       
#     for valor in a:
#         if valor != '':
#             ana = False
#     return print(ana)
# a = input('frase 1: ')
# b = input('frase 2: ')
# result = Anagrama(a,b)

# ex 1
escolha = input('''1. Cadastrar nova turma de alunos para uma nova disciplina
2. Cadastrar novo aluno em uma disciplina existente
3. Remover aluno de uma turma de disciplina
4. Mostrar alunos com maior média da escola
5. Fim:
Escolha: ''')
Disciplinas = ['Algoritmos e Programação', 'Segurança']
Escola = [
  [ ['André Coelho', 19, [7.5, 9.2, 8.9, 6.0]], ['Rebeca Farias', 20, [9.5, 7.8]] ],
  [ ['Tiago Silva', 19, [4.5, 6.1, 7.4]], ['Bárbara Andrade', 18, [5.0, 8.2, 7.6]] ]
]

if escolha == '1':
    def cadastrar_turma(Disciplinas, Escola):
        print("Disciplinas atuais:", Disciplinas)
        
        # Solicita o nome da nova disciplina
        disciplina = input("Disciplina que deseja adicionar: ")
        
        # Verifica se a disciplina já existe
        if disciplina in Disciplinas:
            print(f"A disciplina '{disciplina}' já existe!")
            return  # Sai da função sem cadastrar
        
        Disciplinas.append(disciplina)
        sala = []
        print("Digite 'fim' para encerrar o cadastro de alunos")
        
        nome_aluno = input("Nome do aluno: ")
        while nome_aluno.lower() != 'fim':
            # Verifica se o nome do aluno já existe na sala
            nomes_existentes = [aluno[0] for aluno in sala]
            if nome_aluno not in nomes_existentes:
                aluno = [nome_aluno]
                
                idade = int(input(f"Idade de {nome_aluno}: "))
                aluno.append(idade)
                
                # Cadastro de notas
                notas = []
                n = 0
                while n != -1:
                    n = int(input(f"Digite uma nota de {nome_aluno} (ou -1 para encerrar): "))
                    if n != -1:
                        notas.append(n)
                
                aluno.append(notas)
                sala.append(aluno)
            else:
                print("Aluno já cadastrado na sala!")
            
            nome_aluno = input("Nome do próximo aluno (ou 'fim' para encerrar): ")
        
        # Garante pelo menos um aluno
        if len(sala) == 0:
            print("Você precisa cadastrar pelo menos um aluno!")
            Disciplinas.remove(disciplina)  # Remove disciplina caso não tenha aluno
            return
        
        # Adiciona a sala à escola
        Escola.append({disciplina: sala})
        
        print(f"Turma da disciplina '{disciplina}' cadastrada com sucesso!")
        print("Sala:", sala)
if escolha == '2':
    print(Disciplinas)
    print(Escola)
    #def add(disciplina):
    ind = int(input('Digite o indice da disciplina: '))
    novo_aluno = []
    x = input('Nome do aluno: ')
    
    novo_aluno.append(x)
    y= int(input('Idade: '))
    novo_aluno.append(y)
    n = int(input('Nota do aluno, digite -1 para sair'))
    nota = []
    while n >= 0:
        if n != -1:
            nota.append(n)
        n = int(input('Nota do aluno, digite -1 para sair'))
    novo_aluno.append(nota)
    Escola[ind].append(novo_aluno)