import math
num = int(input("Digite o valor do angulo desejado: "))
angulo = math.radians(num)
sen = math.sin(angulo)
coseno = math.cos(angulo)
tan = math.tan(angulo)
print("O angulo de {}° tem:\nsen = {:.2f}\ncos = {:.2f}\ntangente = {:.2f}".format(num,sen,coseno,tan))