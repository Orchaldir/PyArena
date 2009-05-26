

class Cell:

    def __init__(self, x, y, celltype):
        self.x = x
        self.y = y
        self.type = celltype
        self.creature = None
    
    def draw(self):
        self.type.tile.draw(self.x, self.y)
    
    def is_walkable(self, body):
        return not self.type.solid and self.creature is None    
