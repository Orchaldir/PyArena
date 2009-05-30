import pyglet
from pyglet.gl import *
from pyglet.window import key


from game.action.Move import can_move
from game.map.CellType import CellType
from game.map.Map import Map
from game.object.Creature import Creature
from game.object.body.SimpleBody import SimpleBody
from game.object.controller.Player import Player
from resource.Tile import init_tiles, create_color_tile, create_image_tile


if __name__ == '__main__':
    window = pyglet.window.Window(800, 600, 'PyArena 0.03')   
    
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    init_tiles()
    
    create_color_tile('Grass', 0, 255, 0)
    create_color_tile('Stone', 200, 200, 200) 
    create_image_tile('Fey', 'fey.png')
    create_image_tile('Demon', 'demon.png')    
    
    map = Map()
    map.create(32, 24, CellType('Test', False, 'Grass'))     
    map.get_cell(5, 10).type = CellType('Test', True, 'Stone')
    
    fey = Creature(SimpleBody('Fey'), Player())    
    map.add_creature(fey, 2, 5)
    
    demon = Creature(SimpleBody('Demon'))    
    map.add_creature(demon, 4, 5)
    
    @window.event
    def on_draw():
        fey.controller.execute()
        window.clear()
        map.draw()
    
    @window.event
    def on_key_release(symbol, modifiers):
        if symbol == key.UP:
            can_move(fey, 0)
        elif symbol == key.RIGHT:
            can_move(fey, 1)
        elif symbol == key.DOWN:
            can_move(fey, 2)
        elif symbol == key.LEFT:
            can_move(fey, 3)
  
    pyglet.app.run()
      
