# Construa uma função que receba uma string como parâmetro e devolva outra string com os 
# caracteres embaralhados. Por exemplo: se função receber a palavra python, pode 
# retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize 
# em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, 
# independentemente de como foram digitados

import random

def embaralhar(palavra):
    lista = []
    embaralhado = []
    for caract in palavra:
        lista.append(caract)

    for caract in lista:
        posicao = random.randint(0,len(lista))
        caract = str(caract)
        embaralhado.insert(posicao,caract)

    for caract in embaralhado:
        print(caract,end='')

palavra = str(input("Digite uma palavra: "))
embaralhar(palavra)