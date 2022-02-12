#!/usr/bin/python3

# Name Ditah K
# Program name & Version: Calculator 5
# Date: 15/10/2021
# Version: 2.0


# Prompt the user to quit or for Operator, by passing the string to input function
operator = input('Enter the operator [+, - , *, /] (q to quit): ')

#Prompts user to quit or rerun the program
while (operator != 'q'):

	# If someone puts invalid operator
    if (operator not in '+-*/'):
        operator = input('Invalid operator. Please enter a valid operator: ')
        continue

# Prompt for input and total input numbers can not be less than 2
    numbers = input('Enter space-seperated numbers (min 2): ')
    numbers = numbers.split(' ')

	#Reprompts for numbers, if input is less than 2 numbers
    while (len(numbers) < 2):
        numbers = input('Enter space-seperated numbers (min 2): ')
        numbers = numbers.split(' ')

	#Ignores extra spaces between numbers
    clean_numbers = []
    for number in numbers:
        if (number == ''):
            continue

		#Convers Clean numbers to float
        clean_numbers.append(float(number))
    if (operator == '+'):
        # do addition
        sum = 0
        for number in clean_numbers:
            sum += number
        print(f"-> Result of addition: {sum}")
    elif (operator == '-'):
        # do sub
        sum = clean_numbers[0]
        for i in range(1, len(clean_numbers)):
            sum = sum - clean_numbers[i]
        print(f"-> Result of subtroperator: {sum}")
    elif (operator == '*'):
        # do multiplication
        sum = clean_numbers[0]
        for i in range(1, len(clean_numbers)):
            sum = sum * clean_numbers[i]
        print(f"-> Result of multiplication: {sum}")
    else:
		#If any of the numbers are zero(0), stop and start back at operand
        if (0 in clean_numbers):
            print('Division by zero cannot be performed.')
        else:
			# do division
            sum = clean_numbers[0]
            for i in range(1, len(clean_numbers)):
                sum = sum / clean_numbers[i]
            print(f"-> Result of division: {sum}")

	# Recall the script
    operator = input('Enter the operator [+, - , *, /] (q to quit): ')
    
# Display closing message
print("Thank you for using this program.")
