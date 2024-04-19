n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))
n3 = int(input("Digite o terceiro numero:"))
if n1==n2 and n1==n3 and n2==n3:
    print("São todos iguais")
elif n1>n2 and n1>n3:
    print("O {} é maior".format(n1))
elif n2>n3:
    print("O {} é maior".format(n2))
else:
    print("O {} é maior".format(n3))