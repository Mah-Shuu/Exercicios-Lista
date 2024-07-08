# Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto
# arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de
# poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com
# base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular
# os dados solicitados.

pao=0.12
broa=1.50
venda_paes=int(input("Digite a quantidade de pães vendidos: "))
venda_broa=int(input("Digite a quantidade de broas vendidas: "))

venda_total=venda_paes*pao+venda_broa*broa
poupanca=venda_total*0.1
total=venda_total-poupanca

print(f"Venda total: {venda_total:.2f}\nValor para poupança: {poupanca:.2f}\nValor final: {total:.2f}")