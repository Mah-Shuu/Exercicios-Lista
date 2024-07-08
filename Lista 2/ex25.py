# Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas
# (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois
# valores numéricos e realiza a operação, mostrando o resultado e finalizando o programa

op=int(input("\nSelecione uma operação matemática:\n1 = Soma\n2 = Subtração\n3 = Multiplicação\n4 = Divisão\n"))
num1=float(input("Digite um número: "))
num2=float(input("Digite outro número: "))

if op==1:
    print("\nSoma: ",num1+num2)
elif op==2:
    print("\nSubtração: ",num1-num2)
elif op==3:
    print("\nMultiplicação: ",num1*num2)
elif op==4:
    print("\nDivisão: ",num1/num2)
else:
    print("\nOpção inválida")