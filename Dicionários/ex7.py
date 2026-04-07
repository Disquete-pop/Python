def insere(dic):
    dics = {}
    idiom = input('idioma que deseja adicionar: ')
    esc = 0
    while esc != 1:
        palavra = input('Palavra que Deseja adicionar: ')
        es2 = int(input('Quantas palavras deseja adicionar na tradução dessa palavra?'))
        lista = []
        for valor in range(0,es2):
                lista.append(input(f'Tradução {valor+1}: '))
        dics[palavra] = lista
        esc = int(input('Deseja continuar? digite 0 para sim e 1 para não'))
    dic[idiom] = dics
    print(dic)

def insere_esp(dic):
    idioma = input('idioma: ')
    if idioma in dic:
        dic2 = {}
        lista = []
        palavra = input('Palavra: ')
        quantidade = int(input('Numero de trações que palavra terá'))
        for valor in range(0,quantidade):
            lista.append(input(f'Traduçao {valor+1}: '))
        dic2 = dic[idioma]
        dic2[palavra] = lista
        dic[idioma] = dic2
        print(dic)
    else:
        return 'Idioma inexistente'

def traducoes(dic):
        idio = input('Idioma: ')
        if idio in dic:
             print(dic[idio])

def port(dicio):
    palavra = input('Palavra em portugues que deseja ver a tradução: ')
    idioma = input('idioma: ')
    if dicio[idioma][palavra]:
            print(dicio[idioma][palavra])
    else:
        return 'Palavra não existe'
     
def palavra_outro_id(dic):
    palavra = input('Palavra para ver em portugues: ')
    idioma = input('idioma da palavra: ')
    achado = False
    for valor in dic:
        if idioma == valor:
            dicio = idiomas[valor]
            for chave in dicio:
                if palavra in dicio[chave]:
                    achado = True
                    print(chave)
    if not achado:
         return print('Palavra não econtrada: ')
            
idiomas = {"inglês": {
                        "olá": ["hello", "hi", "hey"],
                        "mundo": ["world"],
                        "gato": ["cat", "kiƩy"]
            },
            "espanhol": {
                            "olá": ["hola", "buenas"],
                            "mundo": ["mundo"],
                            "gato": ["gato", "minino"]
            }
        }

palavra_outro_id(idiomas)