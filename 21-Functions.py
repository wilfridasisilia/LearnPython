# Function = a block of code which is executed only when it is called
def hello(firstname, lastname, ages):
    print("Hellooooooo " + firstname + " " + lastname)
    print("You are " + str(ages) + " years old")
    print("Have a good day")

firstname = input("Enter Your Fist Name: ")
lastname = input("Enter Your Last Name: ")
ages = int(input("How Old Are You: "))
hello(firstname, lastname, ages)
