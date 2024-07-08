# Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e
# escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a
# segunda tabela).

# Preço antigo         Percentual de aumento
# até R$ 50            5%
# entre R$ 50 e R$ 100 10%
# acima de R$ 100      15%

preco=float(input("Digite o valor de um produto: "))

if preco<50:
    print(f"Preço antigo: R${preco:.2f}")
    print(f"Novo preço: R$",preco+preco*0.05)
elif preco>=50 and preco>100:
    print(f"Preço antigo: R${preco:.2f}")
    print(f"Novo preço: R$",preco+preco*0.10)
else:
    print(f"Preço antigo: R${preco:.2f}")
    print(f"Novo preço: R$",preco+preco*0.15)