

class Move:
    
    def __init__(self, obj, direction):
        self.obj = obj
        self.direction = direction
    
    def execute(self):
        if self.obj.body.move(self.direction):
            return True
        
        return False

def can_move(obj, direction):
    if obj is None or obj.body is None or obj.controller is None:
        return False
        
    if obj.body.can_move(direction):
        obj.controller.action = Move(obj, direction)
        return True
    
    return False
