# while loop = a statement that will execute it's block of code
# as long as it's condition remains true
# i = 1
# while i == 1:
#     name = print("Stuck in a loop")

name = ""
# while len(name) == 0:
#     name = input("Enter your name: ")
# or
while not name:
    name = input("Enter your name: ")
print("Hello, " + name)