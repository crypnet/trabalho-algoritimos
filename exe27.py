amount = float(input("Digite a quantidade de litros comprados: "))
type_gas = input("A-alcool, G-gasolina: ")
total =0
discount =0
if type_gas == "A" or type_gas == "a":
	value = 2.1
	if amount <= 20:
		discount = 3
	elif amount > 20:
		discount = 5
elif type_gas == "G" or type_gas == "g":
	value = 3.3
	if amount <= 20:
		discount = 4
	elif amount > 20:
		discount = 6
total = amount*value-(amount*value*discount/100)
print("O valor a ser pago para {} litros de {} é: R$ {}".format(amount,type_gas, total))