import calc
import unittest


class TestCalc(unittest.TestCase):

    def test_add(self):   #must start with test_
        self.assertEqual(calc.add(40,20),60)
        self.assertEqual(calc.add(-1,1),0)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        with self.assertRaises(ValueError):  #or  self.assertRaises(ValueError,calc.divide,10,0)
            calc.divide(10,0)


if __name__ == '__main__':
    unittest.main()

