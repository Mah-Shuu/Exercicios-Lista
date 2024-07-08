# Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela,
# iniciando em 10 e terminando em 0. Mostrar uma mensagem “FIM!” após contagem.

lista=[0,1,2,3,4,5,6,7,8,9,10]
lista.reverse()
i=0

while i<len(lista):
    print(lista[i])
    i+=1
print("FIM!")