#This script generate a multiplication tabel for a user-provided number using a for loop
def main():
    try:
        #Prompt user for input
        number = int(input("Enter a number to see its multiplication table: "))
        #Print multiplication table from 1 to 10
        for i in range(1, 11):
            result = number*i
            print(f"{number} * {i} = {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
#Run the script
if __name__=="__main__":
    main()