# logical operator (and, or, not) is used to check if two or more condition statements is true

temp = int(input("What is the temmprature outside?: "))

# if temp >= 0 and temp <= 30:
#     print("The temprature is good today")
#     print("You can go outside")
# elif temp < 0 or temp > 30:
#     print("The temprature is bad today")
#     print("Please stay inside")

if not (temp >= 0 and temp <= 30):
    print("The temprature is bad today")
    print("Please stay inside")
elif not (temp < 0 or temp > 30):
    print("The temprature is good today")
    print("You can go outside")
