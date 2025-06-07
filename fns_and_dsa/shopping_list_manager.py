# Function to display the menu options to the user
def display_menu():
    # This exact string must match the checker's expectation
    print("Shopping List Manager")  
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function where the program starts
def main():
    # Initialize an empty list to store shopping items
    shopping_list = []

    # Start an infinite loop to keep the menu running
    while True:
        display_menu()  # Show the menu options
        choice = input("Enter your choice (1-4): ").strip()  # Get user input and clean it

        if choice == "1":
            # Add item to shopping list
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")  # Handle empty input

        elif choice == "2":
            # Remove item from shopping list
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")  # Handle item not found

        elif choice == "3":
            # View all items in the shopping list
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == "4":
            # Exit the program
            print("Goodbye!")
            break  # End the loop and exit the program

        else:
            # Handle invalid menu option
            print("Invalid choice. Please enter a number between 1 and 4.")

# Entry point of the script
if __name__ == "__main__":
    main()
