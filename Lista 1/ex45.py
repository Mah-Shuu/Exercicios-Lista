# Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo
# vendida respectivamente por 35, 45 e 55 reais. Construa um algoritmo em que o usuário forneça
# a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina
# informe quanto será o valor arrecadado.

cam_p=35
cam_m=45
cam_g=55

venda_p=int(input("Digite a quantidade de camisas pequenas de uma venda: "))
venda_m=int(input("Digite a quantidade de camisas médias de uma venda: "))
venda_g=int(input("Digite a quantidade de camisas grandes de uma venda: "))

venda_total=(cam_p*venda_p)+(cam_m*venda_m)+(cam_g*venda_g)

print(f"O valor total é: {venda_total}")