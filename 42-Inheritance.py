class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

# THE CLASS YOU INTEND TO BE THE CHILD CLASS MUST SET THE PARENT CLASS
# INSIDE THE PARENTHESES
class Rabit(Animal):
    def run(self):
        print("This rabit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabit = Rabit()
fish = Fish()
hawk = Hawk()

# print(rabit.alive)
# fish.eat()
# hawk.sleep()
rabit.eat()
rabit.run()
fish.swim()
hawk.fly()