import unittest


from Cell import Cell
from CellType import CellType


class Cell_Test(unittest.TestCase):

    def test_init(self):
        type0 = CellType('Test0', True, 'Test')
        type1 = CellType('Test1', False, 'Test')
        
        cell = Cell(0, 0, type0)
        self.assertEqual(cell.x, 0)        
        self.assertEqual(cell.y, 0) 
        self.assertEqual(cell.type, type0) 
        
        cell = Cell(5, 10, type1)
        self.assertEqual(cell.x, 5)        
        self.assertEqual(cell.y, 10) 
        self.assertEqual(cell.type, type1)   


def get_tests():
    return unittest.makeSuite(Cell_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
