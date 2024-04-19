casa = float(input("Digite o valor da casa R$"))
salario = float(input("Digite o valor do salário R$"))
anos = int(input("Quantos anos de financiamento?"))
prestação = casa/(anos*12)
if prestação>(salario*0.3):
    print("Financiamento negado")
else:
    print("Financiamento aprovado")