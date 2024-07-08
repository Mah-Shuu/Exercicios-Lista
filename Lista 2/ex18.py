# Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
# utilizando as seguintes formulas (onde h corresponde à altura):
# • Homens: (72.7∗ h)−58
# • Mulheres: (62,1∗ h)−44,7

h=float(input("Digite sua altura: "))
sexo=str(input("Digite o seu sexo: "))

peso_m=(72.7* h)-58
peso_f=(62.1* h)-44.7

if sexo=="M" or sexo=="m":
    print(f"Seu peso ideal é: {peso_m:.2f}")
elif sexo=="F" or sexo=="f":
    print(f"Seu peso ideal é: {peso_f:.2f}")
else:
    print("Sexo inválido")