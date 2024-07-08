# Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas com 
# pontos de exclamação, conforme o exemplo abaixo (para n = 5):
# !
# !!
# !!!
# !!!! 
# !!!!!

def exclam (linhas):
    print("")
    for linha in range(1,linhas+1):
        print("!"*linha)
    print("")

linhas = int(input("Digite a quantidade de linhas da figura: "))
exclam(linhas)