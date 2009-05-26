import pyglet
from pyglet.gl import *
from pyglet.window import key


from game.map.CellType import CellType
from game.map.Map import Map
from game.object.Creature import Creature
from game.object.body.SimpleBody import SimpleBody
from resource.Tile import init_tiles, create_color_tile, create_image_tile


if __name__ == '__main__':
    window = pyglet.window.Window(800, 600, 'PyArena 0.02')   
    
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    init_tiles()
    
    create_color_tile('Grass', 0, 255, 0)
    create_color_tile('Stone', 200, 200, 200) 
    create_image_tile('Fey', 'fey.png')  
    
    map = Map()
    map.create(32, 24, CellType('Test', False, 'Grass'))     
    map.get_cell(5, 10).type = CellType('Test', True, 'Stone')
    
    creature = Creature(SimpleBody('Fey'))    
    map.add_creature(creature, 2, 5)
    
    @window.event
    def on_draw():
        window.clear()
        map.draw()
    
    @window.event
    def on_key_release(symbol, modifiers):
        if symbol == key.UP:
            creature.body.move(0)
        elif symbol == key.RIGHT:
            creature.body.move(1)
        elif symbol == key.DOWN:
            creature.body.move(2)
        elif symbol == key.LEFT:
            creature.body.move(3)
  
    pyglet.app.run()
      
