

class Creature:

    def __init__(self, body, controller=None):
        self.body = body
        body.object = self
        self.controller = controller
    
    def draw(self):
        self.body.draw()
