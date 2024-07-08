# A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0
# até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame
# final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de
# Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela
# se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 5,9) ou se foi
# aprovado. Crie todas as verificações necessárias.

t_lab=float(input("Digite a nota do trabalho de laboratório: "))
a_bim=float(input("Digite a nota do trabalho de laboratório: "))
ex_final=float(input("Digite a nota do trabalho de laboratório: "))
peso=[2,3,5]
notas=[t_lab,a_bim,ex_final]

nota_ponderada = sum(nota * peso for nota, peso in zip(notas, peso))
media = nota_ponderada / sum(peso)

print(f"\nA média ponderada é: {media}")
if media>=0 and media<3:
    print("Reprovado")
elif media>=3 and media<6:
    print("Recuperação")
else:
    print("Aprovado")