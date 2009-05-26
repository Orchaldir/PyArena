

class Cell:

    def __init__(self, x, y, celltype):
        self.x = x
        self.y = y
        self.type = celltype
    
    def draw(self):
        self.type.tile.draw(self.x, self.y)
        
