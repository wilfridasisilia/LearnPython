# Keyword Arguments = arguments preceded by an identifier when we pass them to a function
# the order of the arguments doesnt matter, unlike positional arguments
# python knows the names of the arguments that our function recieves

def hello(first, middle, last):
    return print("Hello " + first + " " + middle + " " + last)

name = hello(first="wilfrida", last="sisilia", middle="amarise")
hello(name)