def binary_to_hexadecimal(binary_value):
    decimal_value = int(binary_value, 2)
    hexadecimal_result = hex(decimal_value)
    return hexadecimal_result

while True:
    # Input multiple binary values separated by spaces
    binary_values = input("Enter multiple binary values separated by spaces (e.g., 1101 1010 1111): ")
    binary_list = binary_values.replace(",", "").split()

    # Convert each binary value to hexadecimal
    hexadecimal_results = [binary_to_hexadecimal(binary_val) for binary_val in binary_list]

    # Print the results in separate lines with the '0x' prefix
    for result in hexadecimal_results:
        print(result)

    # Ask the user if they want to continue
    user_input = input("Do you want to perform another conversion? (Enter 'y' or 'yes' to continue, 'n' or 'no' to exit): ").lower()

    if user_input not in ['y', 'yes']:
        break
