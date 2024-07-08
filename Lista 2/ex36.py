# Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela´ que
# considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor
# salário terão um aumento proporcionalmente maior do que os funcionários com um salário
# maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus
# adicional de salário. Crie um programa que leia:
# • o valor do salário atual do funcionário;
# • o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).
# Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do
# salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

# Salário Atual    |Reajuste (%) |Tempo de Serviço |Bônus
# Até 500,00       |25%          |Abaixo de 1 ano  |Sem bônus
# Até 1000,00      |20%          |De 1 a 3 anos    |100,00
# Até 1500,00      |15%          |De 4 a 6 anos    |200,00
# Até 2000,00      |10%          |De 7 a 10 anos   |300,00
# Acima de 2000,00 |Sem reajuste |Mais de 10 anos  |500,00

sal_atual=float(input("Digite o valor atual do seu salário: "))
tempo=float(input("Digite seu tempo de serviço em anos: "))

if sal_atual<=500:
    sal_reajuste=sal_atual+sal_atual*0.25
    reajuste=True

elif sal_atual>500 and sal_atual<=1000:
    sal_reajuste=sal_atual+sal_atual*0.20
    reajuste=True

elif sal_atual>1000 and sal_atual<=1500:
    sal_reajuste=sal_atual+sal_atual*0.15
    reajuste=True

elif sal_atual>1500 and sal_atual<=2000:
    sal_reajuste=sal_atual+sal_atual*0.10
    reajuste=True

elif sal_atual>2000:
    sal_reajuste=sal_atual
    reajuste=False

if tempo<1:
    sal_final=sal_reajuste
    bonus=False
elif tempo>=1 and tempo<=3:
    sal_final=sal_reajuste+100
    bonus=True
elif tempo>=4 and tempo<=6:
    sal_final=sal_reajuste+200
    bonus=True
elif tempo>=7 and tempo<=10:
    sal_final=sal_reajuste+300
    bonus=True
elif tempo>10:
    sal_final=sal_reajuste+500
    bonus=True

print(f"\nSalário final: {sal_final:.2f}")
if bonus==True:
    print(f"Bonûs: {sal_final-sal_reajuste}")
else:
    print("Sem bonûs")
if reajuste==True:
    print("Houve reajuste")
else:
    print("Não houve reajuste")