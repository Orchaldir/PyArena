import pyglet


default = None
loader = None
tiles = {}
width = 25
height = 25


class Tile:
    
    def __init__(self, name):
        self.name = name   
        self.image = None       
    
    def draw(self, x, y):
        global width, height
        self.image.blit(x * width, y * height)


class ColorTile(Tile):
    
    def __init__(self, name, r, g, b):
        global width, height
        Tile.__init__(self, name)
        
        self.image = pyglet.image.SolidColorImagePattern((r, g, b, 255)).create_image(width, height)
        
        
class ImageTile(Tile):
    
    def __init__(self, name, image):
        global loader
        
        Tile.__init__(self, name)
        self.image = loader.image(image)
        

def init_tiles():
    global default, loader
    
    default = ColorTile('Default', 255, 0, 255)
    loader = pyglet.resource.Loader(['../data/tiles'])

def create_color_tile(name, r, g, b):
    global tiles
    
    tile = ColorTile(name, r, g, b)
    tiles[name] = tile
    
    return tile

def create_image_tile(name, image):
    global tiles
    
    tile = ImageTile(name, image)
    tiles[name] = tile
    
    return tile

def get_tile(name):
    global default, tiles
    
    if name in tiles:
        return tiles[name]
    
    return default
