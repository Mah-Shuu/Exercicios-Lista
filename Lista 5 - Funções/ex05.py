def maior(n1,n2,n3):
    if n1>n2 and n1>n3:
        maior = n1
    elif n2>n1 and n2>n3:
        maior = n2
    else:
        maior = n3
    
    return maior

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

print(f"Maior número: {maior(n1,n2,n3)}")