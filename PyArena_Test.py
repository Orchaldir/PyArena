import unittest


import game.map.Cell_Test
import game.map.CellType_Test
import game.map.Map_Test
import game.object.body.SimpleBody_Test


if __name__ == "__main__":
    suites = []

    suites.append(game.map.CellType_Test.get_tests())
    suites.append(game.map.Cell_Test.get_tests())
    suites.append(game.map.Map_Test.get_tests())
    
    suites.append(game.object.body.SimpleBody_Test.get_tests())

    suite = unittest.TestSuite(suites)
    
    runner = unittest.TextTestRunner()
    runner.run(suite)  
