# O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do
# distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica,
# de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.

# CUSTO DE FÁBRICA               |% DO DISTRIBUIDOR |% DOS IMPOSTOS
# até R$12.000,00                |5                 |isento
# entre R$12.000,00 e 25.000,00  |10                |15
# acima de R$25.000,00           |15                |20

cus_fab=float(input("Digite o custo de fábrica: "))

if cus_fab<=12000:
    cus_cliente=cus_fab+cus_fab*0.05
    print(f"O valor total é: {cus_cliente}")
elif cus_fab>12000 and cus_fab<25000:
    cus_cliente=cus_fab+cus_fab*0.10+cus_fab*0.15
    print(f"O valor total é: {cus_cliente}")
elif cus_fab>=25000:
    cus_cliente=cus_fab+cus_fab*0.15+cus_fab*0.20
    print(f"O valor total é: {cus_cliente}")
else:
    print(f"O valor total é: {cus_fab}")