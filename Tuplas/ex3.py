'''
A seguinte tabela contém tradução de algumas palavras em
inglês para a língua dos piratas. Escreva um programa que
pergunta ao usuário uma frase em inglês e imprime a tradução da
frase para a língua dos piratas.

'''
dici = {
      'sir' : 'matey',
      'hotel' : 'fleabag inn',
      'student' : 'swabbie',
      'boy' : 'matey',
      'madam' : 'proud beauty',
      'professor' : 'foul blaggart',
      'restaurant' : 'gallery',
      'your' : 'yer',
      'excuse' : 'arr',
      'students' : 'swabbies',
      'are' : 'be',
      'lawyer' : 'foul blaggart',
      'the' : "th'",
      'restroom' : 'head',
      'my' : 'me',
      'hello' : 'avast',
      'is' : 'be',
      'man' : 'matey'

}
busca = str(input('Inglês para Pirateis: ')).lower()
busca += ' '
ac = ''
resultado = ''
lista  = []
for palavra in busca:
    if palavra != ' ':
        ac += palavra
    else:
        if ac != '':
            if ac in dici:
                tradução = dici[ac]
                resultado += tradução + ' '
                ac = ''
            else:
                resultado += ac + ' '
                lista.append(ac)
                ac = ''
print(f'A tradução da frase é :\n', resultado )
if len(lista) > 0:
    print(f'Palavras sem tradução: {lista}')