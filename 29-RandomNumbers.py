import random

x = random.randint(1,6) #between 1 to 6
y = random.random() #between 0 to 1

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","AS"]
random.shuffle(cards)
print(cards)