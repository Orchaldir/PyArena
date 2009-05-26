from resource.Tile import get_tile


class CellType:
    
    def __init__(self, name, solid, tile_name):
        self.name = name        
        self.solid = solid
        
        self.tile = get_tile(tile_name)
