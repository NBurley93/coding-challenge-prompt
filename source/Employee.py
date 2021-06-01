class Employee(object):
    def __init__(self, name: str, salary: int):
        self._name = name
        self._salary = salary


    def get_name(self):
        return self._name


    def get_salary(self):
        return self._salary


    def change_salary(self, amount: int):
        self._salary = amount
    