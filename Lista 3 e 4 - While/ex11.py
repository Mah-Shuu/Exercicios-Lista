# Considerando o intervalo de 0 a 100. Crie um programa que calcule e mostre a soma dos 50
# primeiros números pares.

soma=0
for i in range(0,101,2):
    soma+=i
    
print(soma)