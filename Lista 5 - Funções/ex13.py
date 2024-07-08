# Elabore uma função que receba por parâmetro dois valores X e Z. Calcule e retorne o 
# resultado de XZ para o programa principal. Atenção não utilize nenhuma função pronta de 
# exponenciação

def expo(x,z):
    res = x**z
    return res

x = int(input("Digite um número: "))
z = int(input("Digite outro número: "))

print(f"{x} ^ {z} = {expo(x,z)}")