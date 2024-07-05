#  A lanchonete do Gauchão vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias
# de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo
# ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo
# em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades
# (em quilos) de queijo, presunto e carne necessários para compra.

queijo=50+50
presunto=50
ham=100

quant_sand=int(input("Digite a quantidade de sanduíches aserem feitos: "))
peso_queijo=queijo*quant_sand
peso_presunto=presunto*quant_sand
peso_ham=ham*quant_sand
print(f"Os ingredientes serão:\nQueijo: {peso_queijo}g\nPresunto: {peso_presunto}g\nHambúrguers: {peso_ham}g")
