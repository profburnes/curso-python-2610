import os
os.system("cls")
print("-------------------------------------")
produto = input("Digite o nome do produto:")
valor = float(input("Digite o valor do produto:"))
parcelas = int(input("Digite o nr de parcelas:"))
juros = 1.99

parcela = valor / parcelas
print("O valor de cada parcela sem juros é de {0:.2f}".format(parcela))

total = 0

for i in range(1, parcelas + 1):
    print("Parcela {0}: ". format(i))
    print("Valor: {0:.2f}".format(parcela))
    total = total + parcela
    parcela = parcela + (parcela * juros / 100)

valorJuros = total - valor 
print("O valor total é de R$ {0:.2f}".format(total))
print("O valor dos juros é de R$ {0:.2f}".format(valorJuros))