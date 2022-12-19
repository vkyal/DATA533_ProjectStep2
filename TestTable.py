# Test Table

#from BookMySpot.Data.CustomerInteraction import *
#from BookMySpot.Data.Database import *
#from BookMySpot.Structure.Restaurant import *
from BookMySpot.Structure.Table import *

import unittest



class TestTable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    
    def setUp(self):
        self.table1 =Table('CRAFT','Downtown','Canadian','https://goo.gl/maps/NWo2ELGLaTQYtLJ17',4.3,1683,4,[4,4,4,6])
        self.table2 =Table('Cactus Club','Downtown','Canadian','https://goo.gl/maps/RmsGijZ2kTZ6BSxS6',4.4,1870,4,[8,8,8,8])
        
       
        
    def tearDown(self):
        pass
    
    
    def testAttribute(self):
        self.assertEqual(self.table1.name,'CRAFT')
        self.assertEqual(self.table2.name,'Cactus Club')
        self.assertEqual(self.table1.tables,4)
        self.assertEqual(self.table2.tables,4)
        
    def testClass(self):
        self.assertIsInstance(self.table1,Table)
        self.assertIsInstance(self.table2,Table)
        self.assertIsNot(self.table1,self.table2)
        self.assertIsNotNone(self.table1)
       
    
        
#unittest.main(argv=[''], verbosity=2, exit=False)




