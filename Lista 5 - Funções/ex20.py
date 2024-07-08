# Escreva uma função que gera um triângulo de altura e lados n e base 2*n-1.

def triangulo (linhas):
    cont=0
    print("")
    for linha in range(linhas):
        print(("*"+("*"*(2*cont))).center(linhas*2))
        cont+=1
    print("")

linhas = int(input("Digite a quantidade de linhas da figura: "))
triangulo(linhas)
