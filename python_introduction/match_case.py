"""day = input("Enter a day of the week (monday-sunday): ").lower()

match day:
    case "monday":
        print("ugh, mondays...")
    case "tuesday":
        print("just another workday...")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost there...")
    case "Friday":
        print("TGIF!")
    case "saturday" | "sunday":
        print("weekend vibes!")
    case _:
        print("invalid day entered")



#matching data types
value = input("Enter a value (string or number): ")
match value:
    case int():
        print("you entered an intiger:", value)
    case str():
        print("you entered a string:", value)
    case _:
        print("invalid dat type entered.")"""
    


#demnostreting a guard within a case

"""def has_id(user):
    # Dummy function, define your real logic here
    return True  # or False based on your criteria

user = "example_user"  # Replace this with actual user logic
age = int(input("Enter your age: "))

if age >= 18:
    match age:
        case 18 | 19:
            if has_id(user):
                print("You are eligible to vote.")
            else:
                print("You need a valid ID to vote.")
        case _:
            print("You are eligible to vote.")
else:
    print("You are not yet eligible to vote.")"""



operator = (input("Enter an operator: "))
x = 9
y = 6
match operator:
    case "+":
        result = x + y
    case "-":
        result = x - y
    case "*":
        result = x * y
    case "/":
        result = x / y
    case "_":
        result = "unsupported result"
print(result)



status = int(input("Enter the status code: "))

match status:
    case 200 | 201 | 202:
        print("success")
    case 400 | 401 | 403:
        print("client error")
    case 500 | 501 | 502:
        print("Server error")
    case _:
        print('unkown status')




subject = input("Enter a subject: ")
score = int(input("Enter a score: "))

match subject:
    # if score is 80 or higher in Physics or Chemistry
    case 'Physics' | 'Chemistry' if score >= 80:
        print("Excellent in Science!")
        
    # if score is 80 or higher in English or Grammar
    case 'English' | 'Grammar' if score >= 80:
        print("Excellent in English!")

    # if score is 80 or higher in Maths
    case 'Maths' if score >= 80:
        print("Excellent in Maths!")
        
    case _:
        print(f"Needs improvement in {subject}!")