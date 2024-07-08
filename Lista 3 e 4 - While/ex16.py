# Escreva um programa que leia um número inteiro positivo ímpar N e imprima todos os
# números ímpares de 1 até N em ordem crescente.

lista=[]
num=int(input("Digite um número: "))
if num%2==1:
    i=1
    while i<=num:
        lista.append(i)
        i+=2
    print(lista)

else:
    print("Número não é ímpar")