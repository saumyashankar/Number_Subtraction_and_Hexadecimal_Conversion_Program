# Function to take input from the user
def get_user_input():
    try:
        # Get the first number from the user
        num1 = float(input("Enter the first number: "))
        
        # Get the second number from the user
        num2 = float(input("Enter the second number: "))
        
        return num1, num2
    except ValueError:
        # Handle the case where the user enters non-numeric input
        print("Invalid input. Please enter numeric values.")
        return None, None

# Function to perform the required operations
def perform_operations(num1, num2):
    # Find the larger and smaller numbers
    larger_number = max(num1, num2)
    smaller_number = min(num1, num2)

    # Subtract the smaller number from the larger one
    result = larger_number - smaller_number

    # Convert the result to binary
    binary_result = bin(int(result))

    # Convert the binary result to hexadecimal
    hexadecimal_result = hex(int(binary_result, 2))

    return hexadecimal_result

# Main program
if __name__ == "__main__":
    # Loop to repeat the task
    while True:
        # Get user input
        number1, number2 = get_user_input()

        # Check if input is valid
        if number1 is not None and number2 is not None:
            # Perform operations and get the result
            final_result = perform_operations(number1, number2)

            # Display the final result
            print(f"The result in hexadecimal is: {final_result}")

        # Ask the user if they want to repeat the task
        repeat = input("Do you want to perform another calculation? (y/n): ").lower()

        # Exit the loop if the user does not want to repeat
        if repeat != 'y' and repeat != 'yes':
            break
