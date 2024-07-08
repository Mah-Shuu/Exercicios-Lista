def potencia(base,expoente):
    print("")
    for potencia in range(expoente):
        print(f"{base} ^ {potencia+1} = {base**(potencia+1)}")

base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

potencia(base,expoente)