class Point:
#classes are always start with capitals for each word and don't use underscores
    def __init__(self, x, y): #this method is called a constructor
        self.x = x
        self.y = y

    def move(self):
        print("Move")
                            #classes can have defined methods such as these 2
    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)
print(point.y)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, I am {self.name}")


me = Person("Sam Lowe")
me.talk()

bob = Person("Bob Jones")
bob.talk()