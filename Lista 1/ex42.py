# Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a
# escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.

degrau=float(input("Digite a altura do degrau de uma escada: "))
alt=float(input("Digite a altura que deseja alcançar: "))

res= int(alt/degrau+1)

print(f"A quantidade de degraus a ser subida é: {res}")