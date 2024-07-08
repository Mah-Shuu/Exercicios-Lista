# Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e
# a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a
# cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão
# abaixo:
# Especificação   Código Preço
# Hot Dog         100    12.00
# X-Salada        102    18.50
# X-BACON         103    25.50
# X-Burguer       104    17.00
# Suco de Laranja 105    9.50
# Refrigerante    106    6.00

cod=int(input("Digite o código do produto: "))
quant=int(input("Digite a quantidade: "))

if cod==100:
    valor=12*quant
    print(f"Valor: R${valor:.2f}")
elif cod==102:
    valor=18.5*quant
    print(f"Valor: R${valor:.2f}")
elif cod==103:
    valor=25.5*quant
    print(f"Valor: R${valor:.2f}")
elif cod==104:
    valor=17*quant
    print(f"Valor: R${valor:.2f}")
elif cod==105:
    valor=9.5*quant
    print(f"Valor: R${valor:.2f}")
elif cod==106:
    valor=6*quant
    print(f"Valor: R${valor:.2f}")
else:
    print("Código inválido")