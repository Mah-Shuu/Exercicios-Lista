# Faça um programa que some os números ímpares contidos em um intervalo definido pelo
# usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa
# deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um
# intervalo inválido (começando por um valor maior que o valor final) deve ser escrito uma 
# mensagem de erro na tela, “Intervalo de valores invalido” e o programa´ termina. Exemplo de
# tela de saída:
# Digite o valor inicial e valor final: 5
# 10
# Soma dos ímpares neste intervalo: 21

i=int(input("\nDigite o início do intervalo: "))
f=int(input("Digite o fim do intervalo: "))
par=1
soma=0

if i<f:
    while i<f:
        if i%2==1:
            soma+=i
            i+=1
        else:
            i+=1
            continue
    print(f"Soma de todos os números ímpares do intervalo: {soma}")
        
else:
    print("\nIntervalo de valores inválido\n")
