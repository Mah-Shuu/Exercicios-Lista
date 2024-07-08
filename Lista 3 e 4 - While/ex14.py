# Crie um programa que leia um número inteiro positivo par N e imprima todos os números
# pares de 0 até N em ordem crescente.

n=int(input("Digite um número: "))
if n>=0:
    i=0
    while i<=n:
        print(i)
        i+=2
else:
    print("Número inválido")