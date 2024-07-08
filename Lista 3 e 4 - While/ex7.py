# Escreva um programa que leia 10 inteiros e imprima sua média.

lista=[]
i=0
while i<10:
    lista.append(float(input("Digite um número: ")))
    i+=1

media=sum(lista)/len(lista)
print("Média: ",media)