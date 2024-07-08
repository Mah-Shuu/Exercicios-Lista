# O restaurante a kilo Bem-Bão cobra R$57,00 por cada quilo de refeição. Escreva um algoritmo
# que leia o peso do prato montado pelo cliente (em gramas) e imprima o valor a pagar. Assuma
# que a balança já desconte o peso do prato.

peso=float(input("Digite o peso em gramas do prato: "))
preco_kilo=(peso/1000)*57

print(f"Valor a ser pago: R${preco_kilo}")
