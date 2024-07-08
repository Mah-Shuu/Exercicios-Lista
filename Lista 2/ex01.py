# Crie um programa que leia 2 números inteiros e 1 real. Calcule e mostre: o produto do primeiro
# com a metade do segundo, a soma do triplo do primeiro com o terceiro. O terceiro número
# digitado ao cubo.

num1=int(input())
num2=int(input())
num3=float(input())

res1=num1*(num2/2)
res2=(num1*3)+num3
res3=num3**3

print(f"Resultado 1: {num1}*{num2}/2 = {res1}\nResultado 2: {num1}*3 + {num3} = {res2}\nResultado 3: {num3}^3 = {res3}")