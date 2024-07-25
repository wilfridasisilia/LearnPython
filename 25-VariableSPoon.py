# Scope = the region that variable  is recognize
# a variable is only available from inside the region it is created
# a global and locally scoped versions of a variable can be created

name = "Sisilia" #global scope (available inside the region it is created)
def display_name ():
    name = "Frida"  #local scope (variavle only inside this function
    print(name)

display_name()
print(name)