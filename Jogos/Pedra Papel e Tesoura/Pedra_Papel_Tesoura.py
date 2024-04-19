from random import randint
from time import sleep
itens=('Pedra','Papel','Tesoura')
computador = randint(0,2)
titulo=" Jogo Pedra Papel e Tesoura "
print("{:=^50}".format(titulo))
jogador = int(input('''Escolha uma das opções
0.Pedra
1.Papel
2.Tesoura
Opção: 
'''))
print("-="*30)
print("\033[1;35mO Computador escolheu {}\033[m".format(itens[computador]))
print("\033[2;36mO Jogador escolheu {}\033[m".format(itens[jogador]))
print("-="*30)
ponto = '.'
print("             \033[1;31mR E S U L T A D O\033[m               \n")
sleep(0.5)
if computador==0:
    if jogador==0:
        print("             EMPATE")
    elif jogador==1:
        print("             JOGADOR VENCEU!!")
    elif jogador==2:
        print("             COMPUTADOR VENCEU!!")
    else:
        print("             Operação invalida!!")
elif computador==1:
    if jogador==0:
        print("             COMPUTADOR VENCEU!!")
    elif jogador==1:
        print("             EMPATE")
    elif jogador==2:
        print("             JOGADOR VENCEU!!")
    else:
        print("             Operação invalida!!")
elif computador==2:
    if jogador==0:
        print("             JOGADOR VENCEU!!")
    elif jogador==1:
        print("             COMPUTADOR VENCEU!!")
    elif jogador==2:
        print("             EMPATE")
    else:
        print("             Operação invalida!!")
else:
    print("Operação invalida!!")