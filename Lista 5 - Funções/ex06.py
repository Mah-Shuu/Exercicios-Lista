def reverso(num):
    num = str(num)
    listanum = []
    reversonum = []
    for caract in num:
        listanum.append(caract)

    for caract in listanum:
        reversonum.insert(0,caract)

    for caract in reversonum:
        print(caract,end='')

num = int(input("Digite um número: "))
reverso(num)