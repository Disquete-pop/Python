Lista_geral = []
x = ''
y = ''
while x.lower() != 'fim':
    linha_atual = []
    x = input('Nome do contato: ')
    if x.lower() != 'fim':
        Lista_geral.append(x)
        y = ''
        while y.lower() != 'fim':
            y = input('Numero de telefone: ')
            if y != 'fim':
                linha_atual.append(y)
                Lista_geral.append(linha_atual)
    print(Lista_geral)
a = input('Contato que deseja alterar? (para não alterar digite não): ')  # 2
if a != 'não': 
   for i in range(len(Lista_geral)):
       if Lista_geral[i][0] == a:
           Lista_geral[i][0] = input('Novo contato: ')
print(Lista_geral)

#3

b = input('Numero que deseja deletar (para não alterar digite não): ')
if b != 'não':
   for i in range(len(Lista_geral)):
       if Lista_geral[i][1:] == b:
           del Lista_geral[i][1:]
print(Lista_geral)