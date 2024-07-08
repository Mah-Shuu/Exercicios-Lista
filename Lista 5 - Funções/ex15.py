# Elabore uma função chamada desenhaLinha(). Ele deve desenhar uma linha na tela usando 
# vários símbolos de igual (Ex: ========). A função recebe por parâmetro quantos sinais de igual 
# serão mostrados.

def desenhaLinha(quant):
    linha = ("="*quant)
    return linha

quant = int(input("Digite o tamanho da linha: "))
print(desenhaLinha(quant))