# Crie um programa que leia um número inteiro e, caso ele seja positivo, calcule e mostre:
# • O número digitado ao quadrado;
# • A raiz quadrada do número digitado;

num=int(input("\nDigite um número: "))
print("--"*10)
if num>=0:
    num_quad=num**2
    num_raiz=num**0.5
    print(f"Quadrado do número: {num_quad}\nRaiz quadrada do número: {num_raiz}\n")
else:
    print("Número inválido\n")
