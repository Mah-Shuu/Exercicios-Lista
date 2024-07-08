# Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra 
# for A, a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular a 
# média ponderada, com pesos 5, 3 e 2.

def media(nota1,nota2,nota3):
    op1 = str(input("\nDigite o método:\nA - Média aritmética\nP - Média ponderada\n"))
    op1 = op1.lower()

    if op1 == "a":
        media = (nota1+nota2+nota3)/3
    elif op1 == "p":
        media = ((nota1*5)+(nota2*3)+(nota3*2))/(5+3+2)

    print(f"\nMédia: {media}")

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media(nota1,nota2,nota3)