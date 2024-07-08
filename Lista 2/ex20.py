# Crie um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda
# prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno
# foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.

p1=float(input("Digite a nota da prova 1: "))
p2=float(input("Digite a nota da prova 2: "))
p3=float(input("Digite a nota da prova 3: "))
pt=[p1,p2,p3]
peso=[1,1,2]
nota_ponderada = sum(nota * peso for nota, peso in zip(pt, peso))
media = nota_ponderada / sum(peso)

# media=(p1+p2+p3)/(1+1+2)

print(f"A média ponderada é: {media}")
if media<60:
    print("Reprovado")
else:
    print("Aprovado")