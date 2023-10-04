import unittest
from constructor import Point
class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point = Point(10, 90)
        self.point_2 = Point(4,85)

    def test_move(self):

        self.assertEqual(self.point.move(),'move number 10')
        self.point.x = 30
        self.assertEqual(self.point.move(),'move number 30')

        self.assertEqual(self.point_2.move(), 'move number 4')
        self.point_2.x = 30
        self.assertEqual(self.point_2.move(), 'move number 30')