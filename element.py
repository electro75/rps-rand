import random


# all elements will have a direction they move in defined by y = mx + c
# once they hit a boundary their equation will change (perpendicularly)
#


class Element:
    def __init__(self, kind, x_boundary, y_boundary):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.size = random.randrange(4, 8)
        self.kind = kind

    def __repr__(self):
        return "Element({}, {}, {}, {})".format(self.kind, self.size, self.x, self.y)

    def move(self):
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_y
