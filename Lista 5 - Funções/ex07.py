def vol_esfera(raio):
    pi = 3.14
    volume = (4/3)*pi*(raio**3)

    return volume

raio = int(input("Digite o raio de uma esfera: "))
print(f"Volume da esfera: {vol_esfera(raio):.2f}")