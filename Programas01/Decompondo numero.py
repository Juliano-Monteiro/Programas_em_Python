'''numero = int(input("Digite um numero: "))
n = str(numero)
print("Unidade: {}".format(n[3]))
print("Dezena: {}".format(n[2]))
print("Centena: {}".format(n[1]))
print("Milhar: {}".format(n[0]))'''

#Isso até funciona, porem se vc colocar 3 numeros ou mais de 4 já da problema, então faça assim:

numero = int(input("Digite um numero: "))
u = numero//1%10
d = numero//10%10
c=numero//100%10
m = numero//1000%10
print("Uidad(es): {}".format(u))
print("Dezen(as): {}".format(d))
print("Centen(as): {}".format(c))
print("Milhar(es): {}".format(m))