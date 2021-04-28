import unittest
import question3

class testCaseAdd(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(question3.concatName("Joe","Nibali"),"Joe Nibali")
        self.assertEqual(question3.concatName("Jo n e ","lots of spaces"),"Jo n e  lots of spaces")


if __name__ == '__main__':
    unittest.main()