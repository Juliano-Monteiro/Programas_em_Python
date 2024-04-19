peso = float(input("Digite o seu peso "))
altura = float(input("Digite a sua altura: "))
imc = peso/(altura**2)
print("IMC = {:.2f}".format(imc))
print("Classificação: ")

if imc<18.5:
    print("Magresa")
elif imc<25:
    print("Normal")
elif imc<30:
    print("Sobrepeso")
elif imc<40:
    print("Obesidade")
else:
    print("Obesidade Grave")