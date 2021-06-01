import unittest
from source.Manager import Manager
from source.Employee import Employee

class TestManagerMethods(unittest.TestCase):
    def setUp(self):
        self.manager = Manager('test', 250)
        self.nested_manager = Manager('nested', 250)
        nest2 = Manager('nested2', 250)
        nest2.add_subordinate(Employee('end', 250))
        self.nested_manager.add_subordinate(nest2)

    def test_add_subordinate(self):
        nsub = Employee('testsub', 25)
        self.assertEqual(self.manager.num_subordinates(), 0)
        self.manager.add_subordinate(nsub)
        self.assertEqual(self.manager.num_subordinates(), 1)

    def test_report_salaries(self):
        self.manager.add_subordinate(Employee('testsub', 25))
        self.assertEqual(self.manager.report_salaries(), 275)

    def test_report_salaries_nested(self):
        self.assertEqual(self.nested_manager.report_salaries(), 750)