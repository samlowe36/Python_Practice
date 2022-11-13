class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal): #putting mammal in the paranthesis makes it a parent and dog/cat inherits every single method from it
    def bark(self):
        print("BARK!")


class Cat(Mammal):
    def be_annoying(self):
        print("I am an annoying cat")



dog1 = Dog()
cat1 = Cat()
dog1.walk()
dog1.bark()
cat1.walk()
cat1.be_annoying()