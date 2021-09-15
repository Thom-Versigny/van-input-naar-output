#Thom Versigny pizza calculator
input('Choose a pizza, press enter to continu')
print(""" ----------------------------------------------------
|  Pizza small  : $5.99
|  Pizza medium : $7.99
|  pizza large  : $9.99
 ----------------------------------------------------""")
small = int(input('How many small pizzas do you want? '))
medium = int(input('How many medium pizzas do you want? '))
large = int(input('How many large pizzas do you want? '))
total = 5.99 * small + 7.99 * medium + 9.99 * large

if small <= 10 and medium <= 10 and large <= 10:
	print(f'you chose {small}, small pizzas cost: ${5.99 * small}')
	print(f'you chose {medium}, medium pizzas cost: ${7.99 * medium}')
	print(f'you chose {large}, large pizzas cost: ${9.99 * large}')
	print(f'that will cost in total: ${total}')
	input("Press enter to pay")
else:
	print('We dont deliver that number of pizzas please stay under the 10')
	input('press enter to exit')