# Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma
# de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se
# o número lido não for maior do que zero, o programa termina com a mensagem “Número
# inválido”.

num=(input("Digite um número: "))
num2=int(num)

if(num2>0):
    print(sum(int(i) for i in num))
else:
    print("Número inválido")