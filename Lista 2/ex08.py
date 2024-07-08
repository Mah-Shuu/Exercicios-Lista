# Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do
# número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

num=float(input("Digite um número: "))

if num>=0:
    res=num**0.5
    print(f"A raiz quadrada do número é: {res}")
else:
    print("Número inválido")