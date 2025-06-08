from datetime import datetime, timedelta
# Function to display current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"current date and time: {formatted_date}")
# Function to calculate a future date
def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days = days)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()