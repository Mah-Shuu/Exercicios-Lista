# Crie um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva:
# F - Feminino, M – Masculino ou Sexo Inválido.

genero=str(input("Digite seu gênero (M ou F): "))

if (genero == "M" or genero == "m"):
    print("Masculino")
elif (genero == "F" or genero == "f"):
    print("Feminino")
else:
    print("Sexo inválido")