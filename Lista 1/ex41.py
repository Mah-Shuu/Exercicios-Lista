# Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# • o total a pagar com desconto de 10%;
# • o valor de cada parcela, no parcelamento de 3× sem juros;
# • a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
# • a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

valor=float(input("Digite o valor da venda: "))

pag_vista= valor-valor*0.1
parcela=valor/3

comiss_avista=pag_vista*0.05
comiss_parcel=valor*0.05

print(f"Compra com desconto: {pag_vista}\nParcelas de 3x: {parcela:.2f}\nComissão a vista: {comiss_avista}\nComissão a prazo: {comiss_parcel}")
