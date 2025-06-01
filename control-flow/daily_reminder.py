# Get task details from the user
task = input("Enter yoor task: ").strip()
priority = input("Priority (high/medium/low: )").strip().lower()
time_bound = input("is it time-bound? (yes/no): ").strip().lower()

# Print a separator for clarity
print("\nProcessing your reminder...\n")
# Generate reminder based on priority and time sensivity
match priority:
    case "high":
        if time_bound =="yes":
            print(f"Reminder: '{task}'is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Make sure to handle it soon.")
    case "medium":
        if time_bound =="yes":
            print(f"Reminder: '{task}' is a medium priority task that shoulde be done today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to do it this week.")
    case "low":
        if time_bound =="yes":
            print(f"Reminder: '{task}' is a low priority task that stills needs to be completed today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")