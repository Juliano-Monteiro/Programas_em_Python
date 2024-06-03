num = int(input("Digite o primeiro termo da P.A: "))
razao = int(input("Digite o valor da razão: "))
calculo =0
opr = int(input("Digite a operação desejada\n1.Todos os termos da P.A\n2.Termo especifico\noperação: "))
if opr==1:
    n = int(input("Quantos termos você quer analisar"))
    for i in range(num,n,razao):
        print("{} ".format(i), end=' ')
elif opr==2:
    n = int(input("Qual termo você quer saber: "))
    calculo = (num+(n-1)*razao)
    print("O termo {} da P.A é {}".format(n,calculo))
else:
    print("Operação invalida!")

