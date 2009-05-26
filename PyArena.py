import pyglet


from game.map.CellType import CellType
from game.map.Map import Map
from resource.Tile import init_tiles, create_color_tile, create_image_tile


if __name__ == '__main__':
    window = pyglet.window.Window(800, 600, 'PyArena 0.00')   
    
    init_tiles()
    
    create_color_tile('Grass', 0, 255, 0)
    create_color_tile('Stone', 200, 200, 200)   
    
    map = Map()
    map.create(32, 24, CellType('Test', False, 'Grass'))     
    map.get_cell(5, 10).type = CellType('Test', True, 'Stone')
    
    @window.event
    def on_draw():
        window.clear()
        map.draw()
  
    pyglet.app.run()
      
