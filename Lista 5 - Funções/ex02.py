def data(dia,mes,ano):
    meses=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    mes-=1

    for nome in meses:
        if (mes) == meses.index(nome):
            mes = nome
    
    return (f"{dia} de {mes} de {ano}")

dia = int(input("Digite um dia: "))
while dia not in range(1,31+1):
    dia = int(input("Valor inválido, Digite outro dia: "))
mes = int(input("Digite um mês: "))
while mes not in range(1,12+1):
    dia = int(input("Valor inválido, Digite outro mês: "))
ano = int(input("Digite um ano: "))


print(data(dia,mes,ano))