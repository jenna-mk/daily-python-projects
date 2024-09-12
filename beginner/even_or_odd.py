# Define function to determine whether a number is even or odd
def even_or_odd_num():
    # Allow the user to enter a number 
    num = int(input("Enter a number: "))

    # Check if the number is even or odd
    #! Use the modulus operator %, which gives the remainder of a division
    #! Here we are essentially asking if the input number is divisible by 2
    if num % 2 == 0:
        print(f"The number {num} is odd.")
    else:
        print(f"The number {num} is odd.")

# Return the result 
result = even_or_odd_num()
