import unittest


from game.map.CellType import CellType
from game.map.Map import Map
from game.object.body.SimpleBody import SimpleBody


class SimpleBody_add_to_map_Test(unittest.TestCase):

    def setUp(self):
        self.type0 = CellType('Test', False, 'Test')
        self.type1 = CellType('Test', True, 'Test')
        self.map = Map()
        self.map.create(4, 4, self.type0) 
    
    def test_add_to_map(self):   
        body = SimpleBody(None)
        self.assertTrue(body.add_to_map(self.map, 1, 2))
        self.assertEqual(body.x, 1)  
        self.assertEqual(body.y, 2)  
        self.assertEqual(body.map, self.map)  
    
    def test_occupied(self):
        body0 = SimpleBody(None)
        body0.object = 1
        body0.add_to_map(self.map, 1, 2)
        
        body1 = SimpleBody(None)
        body1.object = 2
        
        self.assertFalse(body1.add_to_map(self.map, 1, 2))
        self.assertEqual(body1.x, None)  
        self.assertEqual(body1.y, None)  
        self.assertEqual(body1.map, None)  
        self.assertEqual(self.map.get_cell(1, 2).creature, 1) 
     
    def test_invalid_cell(self):   
        body = SimpleBody(None)
        self.assertFalse(body.add_to_map(self.map, -1, 0))
        self.assertEqual(body.x, None)  
        self.assertEqual(body.y, None)  
        self.assertEqual(body.map, None)  
    
    def test_solid_cell(self):           
        self.map.get_cell(0, 0).type = self.type1
        
        body = SimpleBody(None)
        self.assertFalse(body.add_to_map(self.map, 0, 0)) 
        self.assertEqual(body.x, None)  
        self.assertEqual(body.y, None)  
        self.assertEqual(body.map, None) 
        self.assertEqual(self.map.get_cell(0, 0).creature, None)         
        

def get_tests():
    return unittest.makeSuite(SimpleBody_add_to_map_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
