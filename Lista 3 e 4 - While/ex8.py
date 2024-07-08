# Escreva um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua
# média.

lista=[]
i=0
while i<10:
    num=int(input("Digite um número: "))
    if num>=0:
        lista.append(num)
    else:
        continue
    i+=1

print(lista)
media=sum(lista)/len(lista)
print("Média: ",media)