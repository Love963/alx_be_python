age = int(input("Enter your age:"))
if age >=18:
    print("You are egilible to vote.")
else:
    print("You are not egilible to vote yet.")








#Discount Calculator with elif
purchase_amount = float(input("Enter your purchase amount: "))

if purchase_amount>=1000:
    discount = 0.1  # 10% discount
elif purchase_amount>=500:
    discount = 0.5  # 5% discoun
else:
    discount = 0  # no discount

final_price = purchase_amount * (1 - discount)
print("final price after discount: $" + str(final_price))

#Letter Grade Assigner with Nested if Statements
score = int(input("Enter your score:"))
if score >=90:
    grade = "A+"
elif score >=80:
    grade ="A"
elif score >=70:
    grade = "B+"
elif score >=65:
    garde ="B"
elif score >=60:
    grade ="B-"
elif score >=50:
    grade ="C+"
elif score >=45:
    grade ="C"
else:
    grade = "F"

print("Your garde is:", grade)



#Even/Odd
number = int(input("Enter the number: "))
if number % 2 ==0:
    print("This is even number.")
else:
    print("This is odd number.")

#Mad libs generator with conditional statement
