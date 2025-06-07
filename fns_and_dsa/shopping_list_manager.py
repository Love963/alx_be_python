# Function to display the menu options
def display_menu():
    print("Shopping List Manager")  # Title of the app
    print("1. Add Item")             # Option to add an item
    print("2. Remove Item")          # Option to remove an item
    print("3. View List")            # Option to view current list
    print("4. Exit")                 # Option to exit the app

# Main function to run the shopping list manager
def main():
    shopping_list = []  # Initialize an empty list to hold shopping items

    while True:
        display_menu()  # Show menu options to the user

        # Ask the user to choose an action
        choice = input("Enter your choice (1-4): ").strip()

        # Option 1: Add an item
        if choice == "1":
            # Prompt user to enter the item to add (must match checker exactly)
            item = input("Enter the item to add: ").strip()
            if item:  # Check that the input is not empty
                shopping_list.append(item)  # Add item to the list
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")

        # Option 2: Remove an item
        elif choice == "2":
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)  # Remove item from the list
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")

        # Option 3: View the list
        elif choice == "3":
            if shopping_list:
                print("\nYour Shopping List:")
                # Enumerate over the list and display each item with index
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        # Option 4: Exit the program
        elif choice == "4":
            print("Goodbye!")
            break  # Exit the loop and end the program

        # Handle invalid input
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the main function only if this file is executed directly
if __name__ == "__main__":
    main()
