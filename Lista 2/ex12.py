# Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim
# como a diferença existente entre ambos.

num1=int(input("\nDigite um número: "))
num2=int(input("Digite outro número: "))

if num1>num2:
    dif=num1-num2
    print(f"Maior: {num1}\nDiferença: {dif}")
else:
    dif=num2-num1
    print(f"Maior: {num2}\nDiferença: {dif}")
