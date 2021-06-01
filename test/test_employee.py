import unittest
from source.Employee import Employee

class TestEmployeeMethods(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('test', 250)

    def test_employee_name(self):
        self.assertEqual(self.employee.get_name(), 'test')

    def test_employee_salary(self):
        self.assertEqual(self.employee.get_salary(), 250)

    def test_employee_change_salary(self):
        self.assertEqual(self.employee.get_salary(), 250)
        self.employee.change_salary(350)
        self.assertEqual(self.employee.get_salary(), 350)