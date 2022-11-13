class Point:
#classes are always start with capitals for each word and dont use underscores
    def move(self):
        print("Move")
                            #classes can have defined methods such as these 2
    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20           #classes can have attributes that we can set anywhere like these point1 and point2 attributes
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)