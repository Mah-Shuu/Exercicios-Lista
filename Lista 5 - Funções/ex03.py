def ver_valor (num):

    if num<0:
        return -1
    elif num>0:
        return 1
    else:
        return 0
    
num = int(input("Digite um número: "))
print(ver_valor(num))