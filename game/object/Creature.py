

class Creature:

    def __init__(self, body):
        self.body = body
        body.object = self
    
    def draw(self):
        self.body.draw()
