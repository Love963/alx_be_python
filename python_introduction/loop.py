fruits = ["banana", "apple", "cherry"]
for fruit in fruits:
    print(fruit)


color =("red", "green", "blue")
for i in color:
    print(i)


message = "Hello, world!"
for character in message:
    print(character)


for number in range(1,6):
    print(number)

for number in range(3,10,2):
    print("Attempt", number, number*".")


successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("Attempted 3 times and failed")

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

for x in "python":
    print(x)


for x in [1,2,3,4,5]:
    print(x)


for number in range(1,20):
    if number % 2 == 0:
        print(number)



numbers =[1, 5, 3, 90]

total =0
for number in numbers:
    total+=number
print("The sum of all numbers is", total)

languages = ["swift", "Go", "Python", "Js"]
for lang in languages:
    print(lang)



#break and continue statement
languages = ["swift", "python", "Go", "C++"]
for lang in languages:
    if lang == "Go":
        break
    print(lang)

languages = ["swift", "python", "Go", "C++"]
for lang in languages:
    if lang == "Go":
        continue
    print(lang)


# outer loop 
attributes = ['Electric', 'Fast']
cars = ['Tesla', 'Porsche', 'Mercedes']

for attribute in attributes:
    for car in cars:
        print(attribute, car)
    
    # this statement is outside the inner loop
    print("-----")
  