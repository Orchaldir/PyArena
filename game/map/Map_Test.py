import unittest


from game.map.CellType import CellType
from game.map.Map import Map


class Map_Test(unittest.TestCase):

    def setUp(self):
        self.type = CellType('Test', False, 'Test')
        self.map = Map()
        self.map.create(2, 4, self.type)          
    
    def test_create(self):
        self.assertEqual(self.map.width, 2)
        self.assertEqual(self.map.height, 4)
        
        for x in range(0, 2):
            for y in range(0, 4):
                cell = self.map.cells[(x,y)]
                self.assertEqual(cell.x, x)
                self.assertEqual(cell.y, y)
                self.assertEqual(cell.type, self.type)

    def test_get_cell(self):
        for x in range(0, 2):
            for y in range(0, 4):
                self.assertEqual(self.map.get_cell(x,y), self.map.cells[(x,y)])  
        
        self.assertEqual(self.map.get_cell(-1,0), None)   
        self.assertEqual(self.map.get_cell(0,-1), None)   
        self.assertEqual(self.map.get_cell(100,0), None)   
        self.assertEqual(self.map.get_cell(0,100), None)   
        self.assertEqual(self.map.get_cell(0,None), None)   
        self.assertEqual(self.map.get_cell(None,0), None)                         


def get_tests():
    return unittest.makeSuite(Map_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
