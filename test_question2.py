import unittest
import question2

class testCaseAdd(unittest.TestCase):
    def test_volume(self):
        lst = {2,2,2}
        lst2 = {0}
        lst3 = {5,5,5,5}
        self.assertEqual(question2.Average(lst),2)
        self.assertEqual(question2.Average(lst2),0)
        self.assertEqual(question2.Average(lst3),5)



if __name__ == '__main__':
    unittest.main()