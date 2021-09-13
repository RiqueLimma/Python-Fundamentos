#
# Arquivo com exemplos de manipulação de  datas
#
from datetime import date
from datetime import time
from datetime import datetime

def ManipulaDataHora():
    hoje = date.today()
    print("Hoje é: ", hoje)
    print("Hoje é: ", hoje.day, hoje.month, hoje.year)      #data separada
    print("Hoje é: ", hoje.weekday())       #mostra os dias da semana em numero o dia que estamos
    dias = ["seg", "ter", "quar", "quin", "sex", "sab", "dom"]
    print("Nome do dia da semana: ", dias[hoje.weekday()])

    data = datetime.now()
    print("data e hora", data)

    tempo = datetime.time(data)
    print ("Hora atual: ", tempo)
    
ManipulaDataHora()