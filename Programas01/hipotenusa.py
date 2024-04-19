'''co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adijacente: "))
hi = (co**2+ca**2)**(1/2)
print("A hipotenusa do triângulo retângulo é {:.2f}".format(hi))'''
import math
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adijacente: "))

'''faz o calculo
da hipotenusa'''

hi = math.hypot(co,ca)
print("A hipotenusa do triângulo retângulo é {:.2f}".format(hi))