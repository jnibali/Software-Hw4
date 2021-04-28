import unittest
import question1

class testCaseAdd(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(question1.cube(3),27)


if __name__ == '__main__':
    unittest.main()