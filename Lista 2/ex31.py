# Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um
# percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:

# | Consumo |(Km/l)|    Mensagem    |
# |menor que|   8  | Venda o carro! |
# |  entre  |8 e 14|   Econômico!   |
# |maior que|  12  |Super econômico!|

km=float(input("Qual foi a distância em Km percorrida: "))
litros=float(input("Qual foi o consumo de gasolina em litros: "))
km_por_l= km/litros

print(km_por_l,"Km/L")
if km_por_l<8:
    print("Venda o carro!")
elif km_por_l>=8 and km_por_l<13:
    print("Econômico!")
else:
    print("Super econômico!")