# Crie uma função que receba a altura e o raio de um cilindro circular e retorne o volume do 
# cilindro. O volume de um cilindro circular e calculado por meio da seguinte fórmula: 
# V = π ∗ raio2 ∗ altura, onde π = 3.141592

def vol_cilindro(altura,raio):
    pi = 3.141592
    volume = pi*(raio**2)*altura

    return volume

raio = float(input("Digite o raio de um cilindro circular: "))
altura = float(input("Digite a altura de um cilindro circular: "))

print(f"Volume do cilindro circular: {vol_cilindro(altura,raio):.2f}")