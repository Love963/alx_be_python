# pattern_drawing.py

# Prompt the user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
i = 0

# Outer while loop for rows
while i < size:
    # Inner for loop for columns
    for j in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after each row
    i += 1
