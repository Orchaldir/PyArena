from Cell import Cell


class Map:

    def __init__(self):
        self.width = 0
        self.height = 0
        self.cells = {}
    
    def create(self, width, height, celltype):
        self.width = width
        self.height = height
        self.cells = {}
        
        for x in range(0, width):
            for y in range(0, height):
                self.cells[(x,y)] = Cell(x, y, celltype)
    
    def draw(self):
        for cell in self.cells.values():
            cell.draw()
    
    def get_cell(self, x, y):
        index = (x,y)
        
        if index in self.cells:
            return self.cells[index]
        
        return None
        
