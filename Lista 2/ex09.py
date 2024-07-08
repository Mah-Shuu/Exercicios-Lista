# Crie um programa que leia dois números. Após a leitura, inverta o valor delas e mostre as mesmas
# com os valores invertidos.

a=float(input("Digite um número (A): "))
b=float(input("Digite um número (B): "))

a2=a-a+b
b2=b-b+a

print(f"A: {a2}\nB: {b2}")