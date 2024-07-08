import math

c1=float(input("Digite o valor do cateto adjacente de um triângulo: "))
c2=float(input("Digite o valor do cateto oposto de um triângulo: "))

### SEM BIBLIOTECA
hip=(c1 ** 2 + c2 ** 2) ** (1/2)

### COM BIBLIOTECA
hip= math.sqrt((c1 ** 2 )+(c2 ** 2))

print(f"A hipotenusa do triângulo é: {hip}")

