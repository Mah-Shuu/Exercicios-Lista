# Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes. A primeira vez deve
# usar a estrutura de repetição for e a segunda while

lista1=[]
lista2=[]
i=0
while i<100:
    lista1.append(i+1)
    i+=1
print(lista1,"\n")

for num in range(100):
    lista2.append(num+1)

print(lista2)

