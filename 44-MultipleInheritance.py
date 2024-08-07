# Multiple Inheritance = when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()