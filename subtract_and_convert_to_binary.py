def subtract_and_convert_to_binary(num1, num2):
    # Find the larger and smaller numbers
    larger_num = max(num1, num2)
    smaller_num = min(num1, num2)

    # Subtract the smaller number from the larger one
    result = larger_num - smaller_num

    # Convert the result to binary
    binary_result = bin(result)[2:]  # [2:] to remove the '0b' prefix in the binary representation

    return binary_result

while True:
    # Input two numbers
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    # Call the function and print the result
    binary_result = subtract_and_convert_to_binary(number1, number2)
    print(f"The binary representation of the difference is: {binary_result}")

    # Ask the user if they want to continue
    user_input = input("Do you want to perform another calculation? (Enter 'y' or 'yes' to continue, 'n' or 'no' to exit): ").lower()

    if user_input not in ['y', 'yes']:
        break
