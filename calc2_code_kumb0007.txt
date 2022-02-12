#!/usr/bin/python3

# Name Ditah Kumbong
# Program name & Version: Calculator 2
# Date: 27/09/2021
# Version: 2.0

# Prompt the user to quit or for Operator, by passing the string to input function
operator = input("Enter Operator : [+, -, *, /, q]: ")

#Prompts user to quit or rerun the program
while (operator != "q"):

# Prompt for first input and convert it to float(decimal)
	first_num = float(input("Enter first number: "))

# Prompt for second input and convert it to float(decimal)
	second_num = float(input("Enter second number: "))

	if (operator == '+'):
		# Do addition and also use f string which allows one to add already existing 		  variable in the middle of the string to be printed
		result = first_num + second_num
		print(f"-> Result of calculation: {first_num} + {second_num} = {result}")
	elif (operator == '-'):
    	# Do subtraction and also use f string
		result = first_num - second_num
		print(f"-> Result of calculation: {first_num} - {second_num} = {result}")
	elif (operator == '*'):
		# Do multiplication and also use f string
		result = first_num * second_num
		print(f"-> Result of calculation: {first_num} * {second_num} = {result}")
	elif (operator == '/'):
		# Do division, special condition and also use f string
		while (second_num == 0):
			second_num = float(input("Can not be 0, Enter something else: "))
		result = first_num / second_num
		print(f"-> Result of calculation: {first_num} / {second_num} = {result}")
	else:
	# If someone puts invalid operator
		print('Invalid operator provided')
# Recall the script
	operator = input("Enter Operator : [+, -, *, /, q]: ")

# Display closing message
print("Thank you for using this program.")


