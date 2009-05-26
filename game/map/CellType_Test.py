import unittest


from CellType import CellType


class CellType_Test(unittest.TestCase):

    def test_init(self):
        
        type = CellType('Test0', True, 'Test')
        self.assertEqual(type.name, 'Test0')        
        self.assertTrue(type.solid)
        
        type = CellType('Test1', False, 'Test')
        self.assertEqual(type.name, 'Test1')        
        self.assertFalse(type.solid)


def get_tests():
    return unittest.makeSuite(CellType_Test, 'test')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(get_tests())  
