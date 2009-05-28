import unittest


from game.map.CellType import CellType
from game.map.Map import Map
from game.object.body.SimpleBody import SimpleBody


class SimpleBody_can_move_Test(unittest.TestCase):

    def setUp(self):
        self.type0 = CellType('Test', False, 'Test')
        self.type1 = CellType('Test', True, 'Test')
        self.map = Map()
        self.map.create(4, 4, self.type0)    
    
    def test_invalid_direction(self): 
        body = SimpleBody(None)  
        body.add_to_map(self.map, 0, 0)   
          
        self.assertFalse(body.can_move(4))  
        self.assertFalse(body.can_move(-1))
        self.assertFalse(body.can_move(None)) 
    
    def test_without_map(self):
        body = SimpleBody(None)     
           
        self.assertFalse(body.can_move(0))
        self.assertFalse(body.can_move(1))
        self.assertFalse(body.can_move(2))
        self.assertFalse(body.can_move(3))
    
    def test_can_move(self):
        body = SimpleBody(None)  
        body.add_to_map(self.map, 1, 1)  
        
        self.assertTrue(body.can_move(0))          
        self.assertTrue(body.can_move(1))  
        self.assertTrue(body.can_move(2))  
        self.assertTrue(body.can_move(3))                 
        
    def test_border(self): 
        body = SimpleBody(None)  
        body.add_to_map(self.map, 0, 0)
        
        self.assertFalse(body.can_move(2))  
        self.assertFalse(body.can_move(3))  
        
        body.add_to_map(self.map, 3, 3)  
        
        self.assertFalse(body.can_move(0))  
        self.assertFalse(body.can_move(1))  
        
    def test_solid_cell(self): 
        body = SimpleBody(None)         
        self.map.get_cell(1, 1).type = self.type1
        
        body.add_to_map(self.map, 1, 0) 
        self.assertFalse(body.can_move(0))  
        
        body.add_to_map(self.map, 0, 1) 
        self.assertFalse(body.can_move(1))
        
        body.add_to_map(self.map, 1, 2) 
        self.assertFalse(body.can_move(2))
        
        body.add_to_map(self.map, 2, 1) 
        self.assertFalse(body.can_move(3))       
        

def get_tests():
    return unittest.makeSuite(SimpleBody_can_move_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
