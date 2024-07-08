# Crie um programa que receba dois números e mostre o maior. Se por acaso, os dois números
# forem iguais, imprima a mensagem: Números iguais.

num1=float(input("Digte um número:"))
num2=float(input("Digte outro número:"))

if num1>num2:
    print(f"Primeiro número ({num1}) é maior")
elif num1<num2:
    print(f"Segundo número ({num2}) é maior")
else:
    print("Números iguais")