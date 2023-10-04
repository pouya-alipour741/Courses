class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        return f'move number {self.x}'
    def draw(self):
        return 'draw'

point = Point(10,20)
print(point.move())
print(point.y)
print(point.draw())


point1 = Point(30,40)
print(point1.x)
print(point1.draw())

