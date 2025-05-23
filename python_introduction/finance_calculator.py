# Prompt the user to enter their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user to enter their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate montholy savings by sabtracting expenses from income
monthly_savings = monthly_income - monthly_expenses

# Calculate annual savings (montholy savings * 12)
# Apply 5% interest on the annual savings
# Formula: total = annual_savings + (annual_savings * 0.05)
annual_savings = monthly_savings * 12
project_annual_savings = annual_savings + (annual_savings * 0.05)

# Print the results
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${project_annual_savings:.0f}.")