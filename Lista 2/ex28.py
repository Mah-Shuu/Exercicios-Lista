# Crie um programa de uma calculadora simples com as 4 operações básicas, apresente o menu
# de opções abaixo, leia dois números reais. Em seguida mostre o resultado da operação entre os
# dois números recebidos. Escreva uma mensagem de erro se a opção for inválida.
# Escolha a opção:
# 1- Soma de 2 números.
# 2- Diferença entre 2 números (maior pelo menor).
# 3- Produto entre 2 números.
# 4- Divisão entre 2 números (o denominador não pode ser zero).

op=int(input("\nEscolha a opção:\n1- Soma de 2 números\n2- Diferença entre 2 números (maior pelo menor).\n3- Produto entre 2 números.\n4- Divisão entre 2 números (o denominador não pode ser zero).\n"))
num1=float(input("Digite um número: "))
num2=float(input("Digite outro número: "))

if op==1:
    print("\nSoma: ",num1+num2)
elif op==2:
    if num1>num2:
        print("\nSubtração: ",num1-num2)
    else:
        print("\nSubtração: ",num2-num1)
elif op==3:
    print("\nMultiplicação: ",num1*num2)
elif op==4:
    if num2>0:
        print("\nDivisão: ",num1/num2)
    else:
        print("Denominador não pode ser zero.")
else:
    print("\nOpção inválida")