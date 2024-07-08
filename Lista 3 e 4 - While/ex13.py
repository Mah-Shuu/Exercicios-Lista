# Crie um programa que leia um número inteiro positivo N e imprima todos os números naturais
# de 0 até N em ordem decrescente.

lista=[]
n=int(input("Digite um número: "))
i=0
while i<=n:
    lista.append(i)
    i+=1

lista.reverse()
i=0
while i<len(lista):
    print(i)
    i+=1