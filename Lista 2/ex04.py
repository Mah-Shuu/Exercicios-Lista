# Crie um programa que receba três números e mostre-os se estão em ordem crescente.

num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))
num3=int(input("Digite o terceiro número: "))

if (num1<num2<num3):
    print("A ordem é crescente")
elif (num1>num2>num3):
    print("A ordem é decrescente")
else:
    print("Não há ordem")