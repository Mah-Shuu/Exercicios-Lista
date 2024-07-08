# Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este
# número. Isto e, janeiro se é 1, fevereiro é 2, e assim por diante.

mes=int(input("Digite um número de 1 à 12: "))

if mes<13 and mes>0:
    if mes==1:
        print("Janeiro")
    elif mes==2:
        print("Fevereiro")
    elif mes==3:
        print("Março")
    elif mes==4:
        print("Abril")
    elif mes==5:
        print("Maio")
    elif mes==6:
        print("Junho")
    elif mes==7:
        print("Julho")
    elif mes==8:
        print("Agosto")
    elif mes==9:
        print("Setembro")
    elif mes==10:
        print("Outubro")
    elif mes==11:
        print("Novembro")
    else:
        print("Dezembro")
else:
    print("Número inválido")