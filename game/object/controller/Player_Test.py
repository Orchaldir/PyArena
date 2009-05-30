import unittest


from game.object.controller.Player import Player

class Action:

    def __init__(self, value):
        self.value = value
        self.number = 0
    
    def execute(self):
        self.number += 1
        return self.value


class Player_Test(unittest.TestCase):

    def test_execute_no_action(self):   
        player = Player()
        self.assertFalse(player.execute())  
    
    def test_execute_action_false(self):   
        player = Player()
        action = Action(False)
        player.action = action
        self.assertFalse(player.execute())
        self.assertEqual(action.number, 1)    
        self.assertEqual(player.action, None)    
    
    def test_execute_action_true(self):   
        player = Player()
        action = Action(True)
        player.action = action
        self.assertTrue(player.execute())
        self.assertEqual(action.number, 1)      
        self.assertEqual(player.action, None)  
        

def get_tests():
    return unittest.makeSuite(Player_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
