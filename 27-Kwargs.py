# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyboard arguments
# (keyword arguments=kwargs)
def hello(**kwargs):
     # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

hello(title="Mr", first="Frida", last="Sisilia")