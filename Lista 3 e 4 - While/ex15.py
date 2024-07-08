# Crie um programa que leia um número inteiro positivo par N e imprima todos os números
# pares de 0 até N em ordem decrescente.

lista=[]
num=int(input("Digite um número: "))
if num%2==0:
    i=0
    while i<=num:
        lista.append(i)
        i+=2
    lista.reverse()
    print(lista)

else:
    print("Número não é par")