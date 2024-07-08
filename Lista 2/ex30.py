# Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma
# taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Crie um programa
# em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço
# final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado
# não for válido, mostrar uma mensagem de erro.

valor=float(input("Digite o valor: "))
estado=str(input("Digite o estado destino do produto (MG, SP, RJ, MS): "))

if estado=="MG":
    print("Valor final: ",valor+valor*0.07)
elif estado=="SP":
    print("Valor final: ",valor+valor*0.12)
elif estado=="RJ":
    print("Valor final: ",valor+valor*0.15)
elif estado=="MS":
    print("Valor final: ",valor+valor*0.08)
else:
    print("Estado inválido")