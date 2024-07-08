idade=int(input("Digite sua idade: "))
ano=int(input("Digite o ano atual: "))
ani=str(input("Fez aniversário esse ano? "))
nascimento=ano-idade

if ani=="sim" or "Sim" == True:
    print(f"Seu ano de nascimento é: {nascimento}")
else:
    nascimento=nascimento-1
    print(f"Seu ano de nascimento é: {nascimento}")
