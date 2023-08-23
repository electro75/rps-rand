import random


# all elements will have a direction they move in defined by y = mx + c
# once they hit a boundary their equation will change (perpendicularly)
# 

class Element:
    def __init__(self, color, x_boundary, y_boundary):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.size = random.randrange(4, 8)
        self.color = color

    def __repr__(self):
        return "Blob({}, {}, {}, {})".format(self.color, self.size, self.x, self.y)
        

    def move(self):
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_y