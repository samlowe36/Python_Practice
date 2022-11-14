import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

members = ["Sam", "Maribel", "Dominic", "Lulu", "Chester", "Coco", "Chippy"]
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)    #rolls first die
        second = random.randint(1,6)    #rolls second die
        return (first, second)      #returns both as a tuple


d6 = Dice()     #create an object of Dice to be used
print(d6.roll())    #print the solution
