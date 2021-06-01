from .Employee import Employee
import operator

class Manager(Employee):
    def __init__(self, name: str, salary: int):
        super().__init__(name=name, salary=salary)
        self._subordinates = list()

    
    def add_subordinate(self, subordinate: Employee):
        self._subordinates.append(subordinate)


    def num_subordinates(self):
        return len(self._subordinates)


    def report_hierarchy(self, level: int = 0):
        # Retrieve a hierarchy list of employees sorted by name
        for e in sorted(self._subordinates, key=operator.attrgetter('_name')):
            print('{0}{1}'.format('\t' * level, e.get_name()))
            if type(e) == Manager:
                e.report_hierarchy(level + 1)


    # Returns a total salary of all subordinate employees
    def report_salaries(self):
        total_salary = 0
        for emp in self._subordinates:
            if type(emp) == Manager:
                total_salary += emp.report_salaries()
            else:
                total_salary += emp.get_salary()
        total_salary += self._salary
        return total_salary