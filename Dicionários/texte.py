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
for valor in idiomas:
    for i in idiomas[valor]:
        print(idiomas[valor])