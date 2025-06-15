def safe_divide(numerator, denominator):
    
    # Attempts to divide two numbers after validating their inputs.
    # Handles division by zero and non-numeric values gracefully.
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Perform division and return result
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
