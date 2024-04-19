num = int(input("digite um numero inteiro: "))
print('''Escolha uma das bases para converção:
1.Binario
2.Octal
3.Hexadecimal
''')
opc = int(input("Opção: "))
if opc ==1:
    print("{} em binario é {}".format(num,bin(num)[2:]))
elif opc == 2:
    print("{} em octal é {}".format(num, oct(num)[2:]))
elif opc == 3:
    print("{} em hexadecimal é {}".format(num, hex(num)[2:]))
else:
    print("Operação invalida!!")
