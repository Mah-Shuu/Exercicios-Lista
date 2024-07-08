# Uma Indústria de Peças automotivas paga R$32,50 por hora normal trabalhada, e R$44,50 por
# hora extra. Faça um algoritmo que leia a quantidade de horas normais trabalhas e a quantidade
# de horas extras. Calcule e imprima o salário bruto e o salário líquido de um determinado
# funcionário. Considere que o salário líquido é igual ao salário bruto descontando-se 11%
# do INSS.

hora_n=float(input("Digite a quantidade de horas normais trabalhadas: "))
hora_ex=float(input("Digite a quantidade de horas extras trabalhadas: "))

sal_bruto=(hora_n*32.50)+(hora_ex*44.50)
sal_liq=sal_bruto-(sal_bruto*0.11)

print(f"Salário bruto: {sal_bruto}\nSalário líquido: {sal_liq}")