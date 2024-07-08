# Elabore uma função que receba dois números inteiros como parâmetros e inicialize uma
# matriz preenchidas de 1 de acordo com os valores recebidos, exemplo:
# criaMatriz(3,3)
# [[1, 1, 1],
# [1, 1, 1],
# [1, 1, 1]]

def criaMatriz(linhas,colunas):
    matriz = []
    for linha in range(linhas):
        lista_linha = []
        for coluna in range(colunas):
            lista_linha.append(1)
        matriz.append(lista_linha)

    return matriz

linhas = int(input("Digite a quantidade de linhas da matriz: "))
colunas = int(input("Digite a quantidade de colunas da matriz: "))
matriz = criaMatriz(linhas,colunas)
print("")
for linha in matriz:
    print(linha)
print("")