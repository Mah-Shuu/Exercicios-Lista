# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

lista=[]
i=0
while i<10:
    lista.append(float(input("Digite um número: ")))
    i+=1

print("Maior número: ",max(lista))
print("Menor número: ",min(lista))