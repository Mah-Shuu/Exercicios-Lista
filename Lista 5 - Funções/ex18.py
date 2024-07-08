# Escreva uma função que gera um triângulo lateral de altura 2*n-1 e n largura. Por exemplo, a 
# saída para n = 4 seria:
# *
# **
# ***
# ****
# ***
# **
# *

def triangulo (linhas):
    cont=2
    print("")
    for linha in range(1,(2*linhas-1)+1):
        if linha>linhas:
            print("*"*(linha-cont))
            cont+=2
            continue
        print("*"*(linha))
        
    print("")

linhas = int(input("Digite a quantidade de linhas da figura: "))
triangulo(linhas)