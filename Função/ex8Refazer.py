def data_mes(Data):
    dias = Data[0:2]
    mes = Data[3:5]
    ano = Data[6:]
    if mes == '01':
        mes == 'Janeiro'
    if mes == '02':
        mes = 'Fevereiro'
    if mes == '03':
        mes = 'Março'
    if mes == '04':
        mes = 'Abril'
    if mes == '05':
        mes = 'Maio'
    if mes == '06':
        mes = 'Junho'
    if mes == '07':
        mes = 'Julho'
    if mes == '08':
        mes = 'Agosto'
    if mes == '09':
        mes = 'Setembro'
    if mes == '10':
        mes = 'Outubro'
    if mes == '11':
        mes = 'Novembro'
    if mes == '12':
        mes = 'Dezembro'
    D = print(f'{dias} de {mes} de {ano}')
    return D
        


Coiso = input('Data desejada no formato dd/nn/aaaa: ')
B = data_mes(Coiso) # retorna um print
