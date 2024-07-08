# Crie um Programa que pergunte em que turno você estuda. Peça para digitar M - Matutino ou V - Vespertino ou N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
# "Valor Inválido!", conforme o caso.

turno=str(input("Digite em que turno você estuda: "))

if (turno == "M" or turno == "m" or turno == "Matutino" or turno=="matutino"):
    print("Bom Dia!")
elif (turno == "V" or turno == "v" or turno == "Vespertino" or turno=="vespertino"):
    print("Boa Tarde!")
elif (turno == "N" or turno == "n" or turno == "Noturno" or turno=="noturno"):
    print("Boa Noite!")
else:
    print("Valor Inválido!")