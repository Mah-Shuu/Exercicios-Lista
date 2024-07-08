# A partir do exercício anterior crie uma função que inicialize uma matriz de 4 x 4, e peça ao
# usuário para preencher com números inteiros. Nesta função você irá passar como parâmetro a
# linha que deseja somar, e retornar a soma dos números armazenados na linha.
# Exemplo:
# criaMatrizUser(2)
# [[10, 20, 30, 40],
# [45, 26, 33, 78],
# [19, 18, 17, 16],
# [13, 14, 15, 16]]
# Soma: 70

def criaMatrizUser(lin):
    global matriz
    matriz = []
    
    for linha in range(4):
        lista_linha = []
        for coluna in range(4):
            num = int(input(f"Digite um número para posição ({linha},{coluna}): "))
            lista_linha.append(num)
        matriz.append(lista_linha)

    return sum(matriz[lin])

linha = int(input("Digite a linha da matriz que quer somar: "))

print("")
print(criaMatrizUser(linha))
print(f"Linha somada: {matriz[linha]}")
print(f"Matriz:")
for linhas in matriz:
    print(linhas)
print("")