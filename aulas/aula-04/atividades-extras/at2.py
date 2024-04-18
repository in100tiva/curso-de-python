def saudacao_horario(horario):
    if 6 <= horario < 12:
        print("Bom dia!")
    elif 12 <= horario < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")

saudacao_horario(11)  # "Bom dia!"
saudacao_horario(17)  # "Boa tarde!"
saudacao_horario(20)  # "Boa noite!"
