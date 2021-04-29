import unittest
import question1

class testCaseAdd(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(question1.cube(3),27)
        self.assertEqual(question1.cube(4),64)
        self.assertEqual(question1.cube(5),125)


if __name__ == '__main__':
    unittest.main()