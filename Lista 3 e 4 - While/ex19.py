# Escreva um algoritmo que leia um número inteiro entre 100 e 9999 e imprima na saída cada um
# dos algarismos que compõem o número.

num=int(input("Digite um número: "))

if num in range(100,10000):
    text=str(num)
    for numero in text:
        print(numero)
else:
    print("Número inválido")