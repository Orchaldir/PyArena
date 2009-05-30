

class Player:

    def __init__(self):
        self.action = None
    
    def execute(self):
        if self.action is not None:
            if self.action.execute():
                self.action = None
                return True
            self.action = None
            
        return False
