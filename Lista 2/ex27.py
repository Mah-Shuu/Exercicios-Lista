# Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo, se
# forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
# • O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
# • Chama-se equilátero o triângulo que tem três lados iguais.
# • Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
# • Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

a=float(input("Digite a medida do lado A de um triangulo: "))
b=float(input("Digite a medida do lado B de um triangulo: "))
c=float(input("Digite a medida do lado C de um triangulo: "))

if a<b+c and b<a+c and c<a+b:
    if a==b and a==c and b==c:
        print("É um triângulo equilátero")
    elif a==b or a==c or c==b:
        print("É um triângulo isóceles")
    elif a!=b and a!=c and b!=c:
        print("É um escaleno")
else:
    print("As medidas não formam um triângulo")