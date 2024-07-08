# Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser
# informado o número de dados lidos e número de valores pares. O processo termina quando for
# digitado o número 0.

par=0
dados=0
i=0
infinito=True
print("Digite 0 para sair")
while infinito==True:
    num=int(input("Digite um número: "))
    if num==0:
        break
        
    dados+=1
    
    if num%2==0 and num!=0:
        par+=1
    

print(f"\nNúmeros lidos: {dados}")
print(f"Números pares lidos: {par}")