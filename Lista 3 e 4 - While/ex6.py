# Escreva um programa que peça ao usuário para digitar 10 valores e some-os

lista=[]
i=0
while i<10:
    lista.append(float(input("Digite um número: ")))
    i+=1

print("Soma dos números:",sum(lista))