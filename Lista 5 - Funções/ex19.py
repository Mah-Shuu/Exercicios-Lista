# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
# e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda
# função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

import random
numeros = []

def sorteio():
    for vezes in range(5):
        num = random.randint(0,10)
        numeros.append(num)

    return numeros

def somaPar():
    soma = 0
    for numero in numeros:
        if numero%2==0:
            soma+=numero
        else:
            continue

    return soma

sorteio()
print(f"{numeros}\n{somaPar()}")