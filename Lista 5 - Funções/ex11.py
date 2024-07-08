#  Elabore uma função que receba dois valores numéricos e um símbolo. Este símbolo representara 
# a operação que se deseja efetuar com os números. Se o símbolo for + deverá ser realizada uma 
# adição, se for − uma subtração, se for / uma divisão e se for ∗ será efetuada uma multiplicação.

def calculadora(n1,n2,op):
    if op=="+":
        res=n1+n2
    elif op=="-":
        res=n1-n2
    elif op=="/":
        res=n1/n2
    elif op=="*":
        res=n1*n2
    else:
        return "Operação inválida"
    
    return res

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
op = str(input("\nDigite uma das seguintes opçãoes:\n+ = Adição\n- = Subtração\n/ = Divisão\n* = Multiplicação\n"))

print(calculadora(num1,num2,op))