# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the " + item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item)) #postional arguments
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) #keyword argument

text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Frida"
print("Hello my name is {}".format(name))
print("Hello my name is {:10}. Nice to meet you".format(name))
print("Hello my name is {:<10}. Nice to meet you".format(name)) #left
print("Hello my name is {:>10}. Nice to meet you".format(name)) #right
print("Hello my name is {:^10}. Nice to meet you".format(name)) #center

number = 1000
print("The number of pi is {:.2f}".format(number)) #2 digit floating point
print("The number of is {:,}".format(number)) #
print("The number of is {:b}".format(number)) #binary
print("The number of is {:o}".format(number)) #octo
print("The number of is {:x}".format(number)) #hexadesimal
print("The number of is {:e}".format(number)) #scientific/lowercase
print("The number of is {:E}".format(number)) #scientific/uppercase
