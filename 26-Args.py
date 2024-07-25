# *args = parameter that will pack all argumnets into a
# tuple useful so that a fuction can accept a varying amount of arguments

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
       sum += i
    return sum

print(add(1,2,3,4,5,6,7,8))