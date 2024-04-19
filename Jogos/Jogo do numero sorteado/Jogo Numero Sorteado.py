import random
sorteado = random.randint(1,5)
numero=int(input("Digie o numero que você acha que foi sorteado de 1 a 5: "))
if numero<sorteado:
    print("O numero é menor  que esse")
elif numero == sorteado:
    print("É esse!")
else:
    print("è maior que esse")