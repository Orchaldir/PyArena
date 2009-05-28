import unittest


from game.map.CellType import CellType
from game.map.Map import Map
from game.object.body.SimpleBody import SimpleBody


class SimpleBody_move_Test(unittest.TestCase):

    def setUp(self):
        self.type0 = CellType('Test', False, 'Test')
        self.type1 = CellType('Test', True, 'Test')
        self.map = Map()
        self.map.create(4, 4, self.type0)    
    
    def test_without_map(self):
        body = SimpleBody(None)        
        self.assertFalse(body.move(0))
        self.assertFalse(body.move(1))
        self.assertFalse(body.move(2))
        self.assertFalse(body.move(3))
    
    def test_occupied(self):
        body0 = SimpleBody(None)   
        body0.object = 1 
        body0.add_to_map(self.map, 1, 1)  
        
        body1 = SimpleBody(None) 
        body1.object = 2              
        body1.add_to_map(self.map, 1, 0) 
        
        self.assertFalse(body1.move(0))   
        self.assertEqual(body1.x, 1)  
        self.assertEqual(body1.y, 0)  
        self.assertEqual(self.map.get_cell(1, 0).creature, 2) 
        
        self.assertEqual(body0.x, 1)  
        self.assertEqual(body0.y, 1)  
        self.assertEqual(self.map.get_cell(1, 1).creature, 1) 
    
    def test_move(self):
        body = SimpleBody(None)  
        body.add_to_map(self.map, 0, 0)  
        
        self.assertTrue(body.move(0))  
        self.assertEqual(body.x, 0)  
        self.assertEqual(body.y, 1)  
        self.assertEqual(body.map, self.map) 
        
        self.assertTrue(body.move(1))  
        self.assertEqual(body.x, 1)  
        self.assertEqual(body.y, 1)  
        self.assertEqual(body.map, self.map) 
        
        self.assertTrue(body.move(2))  
        self.assertEqual(body.x, 1)  
        self.assertEqual(body.y, 0)  
        self.assertEqual(body.map, self.map)      
        
        self.assertTrue(body.move(3))  
        self.assertEqual(body.x, 0)  
        self.assertEqual(body.y, 0)  
        self.assertEqual(body.map, self.map) 
                
    def test_invalid_direction(self): 
        body = SimpleBody(None)  
        body.add_to_map(self.map, 0, 0)   
          
        self.assertFalse(body.move(4))  
        self.assertEqual(body.x, 0)  
        self.assertEqual(body.y, 0)  
        self.assertEqual(body.map, self.map) 
        
    def test_border(self): 
        body = SimpleBody(None)  
        body.add_to_map(self.map, 0, 0)
        
        self.assertFalse(body.move(2))  
        self.assertEqual(body.x, 0)  
        self.assertEqual(body.y, 0)  
        self.assertEqual(body.map, self.map)      
        
    def test_solid_cell(self): 
        body = SimpleBody(None)         
        self.map.get_cell(1, 1).type = self.type1
        
        body.add_to_map(self.map, 1, 0) 
        self.assertFalse(body.move(0))   
        self.assertEqual(body.x, 1)  
        self.assertEqual(body.y, 0)          
        

def get_tests():
    return unittest.makeSuite(SimpleBody_move_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
