import unittest


from game.map.CellType import CellType
from game.map.Map import Map
from game.object.body.SimpleBody import SimpleBody


class SimpleBody_Test(unittest.TestCase):

    def setUp(self):
        self.type0 = CellType('Test', False, 'Test')
        self.type1 = CellType('Test', True, 'Test')
        self.map = Map()
        self.map.create(4, 4, self.type0) 
    
    def test_add_to_map(self):
        body0 = SimpleBody(None)
        body0.object = 1
        self.assertTrue(body0.add_to_map(self.map, 1, 2))
        self.assertEqual(body0.x, 1)  
        self.assertEqual(body0.y, 2)  
        self.assertEqual(body0.map, self.map) 
        
        body1 = SimpleBody(None)
        body1.object = 1
        self.assertFalse(body1.add_to_map(self.map, 1, 2))
        self.assertEqual(body1.x, None)  
        self.assertEqual(body1.y, None)  
        self.assertEqual(body1.map, None)  
     
    def test_add_to_invalid_cell(self):   
        body = SimpleBody(None)
        self.assertFalse(body.add_to_map(self.map, -1, 0))
        self.assertEqual(body.x, None)  
        self.assertEqual(body.y, None)  
        self.assertEqual(body.map, None)  
    
    def test_add_to_solid_cell(self):           
        self.map.get_cell(0, 0).type = self.type1
        
        body = SimpleBody(None)
        self.assertFalse(body.add_to_map(self.map, 0, 0)) 
        self.assertEqual(body.x, None)  
        self.assertEqual(body.y, None)  
        self.assertEqual(body.map, None) 
    
    def test_get_type(self):
        body = SimpleBody(None)        
        self.assertEqual(body.get_type(), 'Simple')     
    
    def test_move_without_map(self):
        body = SimpleBody(None)        
        self.assertFalse(body.move(0))
        self.assertFalse(body.move(1))
        self.assertFalse(body.move(2))
        self.assertFalse(body.move(3))
    
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
                
    def test_move_invalid_direction(self): 
        body = SimpleBody(None)  
        body.add_to_map(self.map, 0, 0)   
          
        self.assertFalse(body.move(4))  
        self.assertEqual(body.x, 0)  
        self.assertEqual(body.y, 0)  
        self.assertEqual(body.map, self.map) 
        
    def test_move_outside_map(self): 
        body = SimpleBody(None)  
        body.add_to_map(self.map, 0, 0)
        
        self.assertFalse(body.move(2))  
        self.assertEqual(body.x, 0)  
        self.assertEqual(body.y, 0)  
        self.assertEqual(body.map, self.map)      
        
        self.assertFalse(body.move(3))  
        self.assertEqual(body.x, 0)  
        self.assertEqual(body.y, 0)  
        self.assertEqual(body.map, self.map) 
        
        body.add_to_map(self.map, 3, 3)  
        
        self.assertFalse(body.move(0))  
        self.assertEqual(body.x, 3)  
        self.assertEqual(body.y, 3)  
        self.assertEqual(body.map, self.map) 
        
        self.assertFalse(body.move(1))  
        self.assertEqual(body.x, 3)  
        self.assertEqual(body.y, 3)  
        self.assertEqual(body.map, self.map) 
        
    def test_move_solid_cell(self): 
        body = SimpleBody(None)         
        self.map.get_cell(1, 1).type = self.type1
        
        body.add_to_map(self.map, 1, 0) 
        self.assertFalse(body.move(0))   
        self.assertEqual(body.x, 1)  
        self.assertEqual(body.y, 0)  
        
        body.add_to_map(self.map, 0, 1) 
        self.assertFalse(body.move(1))
        self.assertEqual(body.x, 0)  
        self.assertEqual(body.y, 1)  
        
        body.add_to_map(self.map, 1, 2) 
        self.assertFalse(body.move(2))
        self.assertEqual(body.x, 1)  
        self.assertEqual(body.y, 2)  
        
        body.add_to_map(self.map, 2, 1) 
        self.assertFalse(body.move(3))
        self.assertEqual(body.x, 2)  
        self.assertEqual(body.y, 1)          
        

def get_tests():
    return unittest.makeSuite(SimpleBody_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
