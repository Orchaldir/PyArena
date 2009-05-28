from resource.Tile import get_tile


class SimpleBody:

    direction_x = [0, 1, 0, -1]
    direction_y = [1, 0, -1, 0]

    def __init__(self, tile_name):
        self.x = None
        self.y = None
        self.map = None
        
        self.tile = get_tile(tile_name)
        self.object = None
    
    def add_to_map(self, map, x, y):
        cell = map.get_cell(x, y)
        
        if cell is None or not cell.is_walkable(self):        
            return False
        
        self.x = x
        self.y = y
        self.map = map
        cell.creature = self.object
        
        return True
    
    def can_move(self, direction, cell=None):
        if self.map is None or direction < 0 or direction >= 4:        
            return False
        
        new_x = self.x + SimpleBody.direction_x[direction]
        new_y = self.y + SimpleBody.direction_y[direction]
        
        cell = self.map.get_cell(new_x, new_y)
        
        if cell is None or not cell.is_walkable(self):         
            return False
        
        return True 
    
    def draw(self):
        self.tile.draw(self.x, self.y)
    
    def get_type(self):
        return 'Simple'
    
    def move(self, direction):
        if self.map is None or direction < 0 or direction >= 4:        
            return False
        
        new_x = self.x + SimpleBody.direction_x[direction]
        new_y = self.y + SimpleBody.direction_y[direction]
        
        cell = self.map.get_cell(new_x, new_y)
        
        if cell is None or not cell.is_walkable(self):         
            return False
        
        old_cell = self.map.get_cell(self.x, self.y)
        old_cell.creature = None
        
        self.x = new_x
        self.y = new_y
        cell.creature = self.object
        
        return True 
