carros = ["Fusca","Corcel","Fiat 147","Marea"]
print(carros[0])
print("Mostrando todos os veiculos")

carros.append("Opala")

novoCarro = input("Digite um novo veículo: ")
carros.append(novoCarro)

carros.sort()

x = 1
for carro in carros:
    print("O {0}º carro é o {1}".format(x, carro))
    x += 1