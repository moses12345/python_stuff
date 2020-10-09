import unittest
from findindmissing import finding

class Testingfinding(unittest.TestCase):
    def test_finding(self):
        self.assertEqual(finding([1,5]),[2,3,4])
        self.assertEqual(finding([1,3]),[2])
        
if __name__ =="__main__":
    unittest.main()        