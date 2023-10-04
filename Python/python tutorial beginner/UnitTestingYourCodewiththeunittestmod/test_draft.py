from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp1 = Employee('pouya','alipour',6500)
    def test_email(self):
        self.assertEqual(self.emp1.email,'pouya.alipour@email.com')
        self.emp1.first = 'john'
        self.assertEqual(self.emp1.email,'john.alipour@email.com')

