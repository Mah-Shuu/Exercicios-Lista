# Em uma empresa paga-se R$ 40,50 a hora e recolhe-se para o imposto de renda 11% dos salários
# acima de R$ 2500,00. Dado o número de horas trabalhadas por um funcionário, informar o valor
# do seu salário líquido.

hora=int(input("\nDigite o número de horas trabalhadas: "))
sal_bruto=hora*40.50

if sal_bruto>0:
    if sal_bruto<=2500:
        print(f"\nSalário líquido: {sal_bruto}\n")
    else:
        sal_liq=sal_bruto-sal_bruto*0.11
        print(f"\nSalário bruto: {sal_bruto}")
        print(f"Salário líquido: {sal_liq}\n")
else:
    print("Número inválido\n")