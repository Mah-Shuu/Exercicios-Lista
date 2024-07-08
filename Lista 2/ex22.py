# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente
# a este número. Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante.

dia=int(input("Digite um número de 1 à 7: "))

if dia<8 and dia>0:
    if dia==1:
        print("DOMINGO")
    elif dia==2:
        print("SEGUNDA-FEIRA")
    elif dia==3:
        print("TERÇA-FEIRA")
    elif dia==4:
        print("QUARTA-FEIRA")
    elif dia==5:
        print("QUINTA-FEIRA")
    elif dia==6:
        print("SEXTA-FEIRA")
    else:
        print("SÁBADO")
else:
    print("Número inválido")