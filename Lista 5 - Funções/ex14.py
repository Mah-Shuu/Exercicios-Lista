# Elabore uma função que receba a distância em Km e a quantidade de litros de gasolina 
# consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma 
# mensagem de acordo com a tabela abaixo:

def gasto(dis,litros):
    kmporlitro=dis/litros
    if kmporlitro<8:
        msg = "Gasta muito!"
    elif kmporlitro >=8 and kmporlitro <=15:
        msg = "Econômico!"
    else:
        msg = "Super econômico!"

    return msg

km = float(input("Digite uma distância em Km de um percurso: "))
litros = int(input("Digite a quantidade de litros gastos por um carro no percurso: "))

print(gasto(km,litros))