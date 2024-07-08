#  Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que
# esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de
# imposto sobre o salário-base.

salairio_base = float(input("Digite o salário base de um funcionário: "))
sal_grat = salairio_base + salairio_base * 0.05
sal_imposto = sal_grat - salairio_base * 0.07
print(f"O salário a receber é: {sal_imposto}")