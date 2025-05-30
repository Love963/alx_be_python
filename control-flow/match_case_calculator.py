# Prompts user for two numbers and an operation (+, -, *, /)

def main():
    try:
        # Prompt user to enter two integers
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Prompt for operation choice
        operation = input("Choose the operation (+, -, *, /): ")

        # Perform calculation using match-case
        match operation:
            case "+":
                result = num1 + num2
                print(f"The result is {result}.")
            case "-":
                result = num1 - num2
                print(f"The result is {result}.")
            case "*":
                result = num1 * num2
                print(f"The result is {result}.")
            case "/":
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"The result is {result}.")
            case _:
                print("Invalid operation.")
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")

# Run the calculator when the script is executed directly
if __name__ == "__main__":
    main()
