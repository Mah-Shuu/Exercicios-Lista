# Crie uma função que receba uma temperatura em graus Celsius e retorne-a convertida em graus 
# Fahrenheit. A fórmula de conversão é: F = C ∗ (9.0/5.0) + 32.0, sendo F a temperatura em 
# Fahrenheit e C a temperatura em Celsius.

def fahrenheit(celsius):

    convert = celsius*(9/5)+32

    return convert

grau = float(input("Digite uma temperatura em Celsius: "))

print(f"Conversão para Fahrenheit: {fahrenheit(grau)}")