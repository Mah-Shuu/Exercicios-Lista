# A fábrica de refrigerantes Frutuba vende seu produto em três formatos: lata de 350 ml,
# garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma determinada
# quantidade de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele
# comprou.

venda_lata=int(input("Digite a quantidade de latas 350ml gostaria de comprar: "))
venda_g600=int(input("Digite a quantidade de garrafas 600ml gostaria de comprar: "))
venda_g2l=int(input("Digite a quantidade de garrafas 2L gostaria de comprar: "))

lata=venda_lata*350
garrafa_600=venda_g600*600
garrafa_2l=venda_g2l*2000

total=(lata+garrafa_2l+garrafa_600)/1000

print(f"A quantidade total em litros de refrigerante é: {total}L")