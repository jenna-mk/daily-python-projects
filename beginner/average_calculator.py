# Define function to calculate the average of three numbers
def calculate_avg():
    # Prompt the user to input three numbers
    #! Use the input() comment, which takes an input from the user and returns it as a string
    #! **SYNTAX** input(prompt), where prompt = a string displayed on the string (optional)
    #! NOTE: Since the user input is always returned as a string, it needs to be converted if you want a different data type (here, we use float())
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Calculate the average 
    average = (num1 + num2 + num3) / 3

    # Return the average
    #! Use the round() function to restrict to 2 decimal points
    #! **SYNTAX** round(number, digits), where number = number to be rounded (required) and digits = number of decimals (optional - default is 0)
    return round(average, 2) 

# Call the function and display the result
result = calculate_avg()
print(f"The average of the three numbers is: {result}")
