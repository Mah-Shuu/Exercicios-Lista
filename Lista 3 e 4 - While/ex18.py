# Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles. A
# quantidade de números a serem lidos deve será fornecida pelo usuário.

lista=[]
i=0
quant=int(input("Digite o tamanho da lista: "))
while i<quant:
    print(f"({i+1})",end=" ")
    lista.append(float(input("Digite um número: ")))
    i+=1

print("\nMaior número: ",max(lista))
