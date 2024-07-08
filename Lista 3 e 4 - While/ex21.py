# Crie um programa que receba dois números. Calcule e mostre:
# • a soma dos números pares desse intervalo de números, incluindo os números digitados;
# • a multiplicação dos números ímpares desse intervalo, incluindo os digitados;

num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
soma=0
mult=1


for num in range(num1,num2+1):
    if num%2==0:
        soma+=num
    else:
        mult*=num
        print(num)

print(f"Soma dos números pares: {soma}")
print(f"Multiplicação dos números ímpares: {mult}")

