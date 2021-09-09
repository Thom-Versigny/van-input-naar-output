#Thom Versigny pizza calculator
small = 1
medium = 2
large = 3
input('Choose a pizza, press enter to continu')
print(""" ----------------------------------------------------
|  Pizza small  : $5.99
|  Pizza medium : $7.99
|  pizza large  : $9.99
 ----------------------------------------------------""")
size = int(input('Choose the size: small press 1, medium press 2, large press 3: '))
muchpizza = int(input('How many pizzas do you want? '))
if size == small and muchpizza < 10:
	print('you chose ',muchpizza,', small pizzas that will cost you:',5.99 * muchpizza,'$')
	input("Press enter to pay")

if size == medium and muchpizza < 10:
	print('you chose ',muchpizza,', medium pizzas that will cost you:',7.99 * muchpizza,'$')
	input("Press enter to pay")

if size == large and muchpizza < 10:
	print('you chose ',muchpizza,', large pizzas that will cost you:',9.99 * muchpizza,'$')
	input("Press enter to pay")

if size > large or muchpizza > 10:
	print("Sorry, we dont deliver that kind/number of pizza")
	input('press enter to exit')

