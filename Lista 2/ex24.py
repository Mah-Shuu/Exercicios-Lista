# Crie um programa que calcule e mostre a área de um trapézio. Sabe-se que:
# A=(a+b)h/2
# Lembre-se a base maior e a base menor devem ser números maiores que zero.


b_maior=float(input("Digite a medida da base maior: "))

if b_maior>0:
    b_menor=float(input("Digite a medida da base menor: "))

    if b_menor>0:
        h=float(input("Digite a medida da altura: "))

        a=((b_maior+b_menor)*h)/2
        print(f"A área do trapézio é: {a}")
    else:
        print("Base menor inválida")
else:
    print("Base maior inválida")