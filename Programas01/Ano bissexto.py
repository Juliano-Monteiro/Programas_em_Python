import datetime
ano = int(input("Digite o ano que deseja analisar. Coloque 0 para ver o ano atual: "))
if ano==0: # Pega o ano atual
    ano = datetime.date.today().year
if ano%4==0 and ano%100 != 0 or ano%400 ==0: # vê se o ano digitado é bissexto
    print("O ano {} é bissexto!!".format(ano))
else:
    print("Não é bissexto :(".format(ano))