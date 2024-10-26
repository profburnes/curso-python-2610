import os
os.system("cls")

frutas = ['Siriguela']

def menu():
    os.system("cls")
    print("-----------------------------------------")
    print("----------- Menu Principal --------------")
    print("-----------------------------------------")
    print("| Digite 1 para inserir uma nova fruta  |")
    print("| Digite 2 para mostrar as frutas       |")
    print("| Digite 3 para excluir uma fruta       |")
    print("| Digite 4 para sair dp sistema         |")
    print("-----------------------------------------")
    opcao = input("Digite a opção desejada: ")
    if (opcao == "1"):
        inserirFruta()
    elif (opcao == "2"):
        mostrarFrutas()
    elif (opcao == "3"):
        excluirFruta()
    else:
        sair()

def mostrarOpcoes():
    tecla = input("Se vc deseja voltar ao menu, pressione 1, se vc deseja sair, pressione 2: ")
    if (tecla == "1"):
        menu()
    elif (tecla == "2"):
        sair()
    else:
        mostrarOpcoes()

def sair():
    print("Hasta la vista baby....")

def inserirFruta():
    fruta = input("Digite o nome de uma fruta: ")
    frutas.append(fruta)
    mostrarOpcoes()

def excluirFruta():
    fruta = input("Digite o nome da fruta: ")
    frutas.remove(fruta)
    mostrarOpcoes()

def mostrarFrutas():
    i = 1
    frutas.sort()
    for fruta in frutas:
        print("Fruta {0}: {1}".format(i, fruta))
        i += 1
    mostrarOpcoes()

menu()