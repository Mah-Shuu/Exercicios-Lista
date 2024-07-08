# Elabore uma função que receba dois números inteiros positivos por parâmetros e retorne a
# soma dos N números inteiros existentes entre eles.

def soma(n1,n2):
    lista = []
    for num in range(n1+1,n2):
        lista.append(num)
        
    soma = sum(lista)
    return soma

n1=int(input("Digite um número: "))
while n1<0:
    n1 = int(input("Valor inválido, Digite outro número: "))
    
n2=int(input("Digite outro número: "))
while n2<0:
    n2 = int(input("Valor inválido, Digite outro número: "))

print(f"Soma dos valores entre o número {n1} e {n2}: {soma(n1,n2)}")