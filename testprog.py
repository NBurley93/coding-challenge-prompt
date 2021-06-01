from source.Manager import Manager
from source.Employee import Employee
import json
import sys
import os


def parse_employee(emp: dict):
    name = 'UNDEFINED'
    salary = 0
    subordinates = []
    is_manager = False

    if 'name' in emp.keys():
        name = emp['name']

    if 'salary' in emp.keys():
        salary = emp['salary']

    if 'employees' in emp.keys():
        is_manager = True
        subordinates = [parse_employee(x) for x in emp['employees']]

    if is_manager:
        # Create manager
        mgr = Manager(name, salary)
        for s in subordinates:
            mgr.add_subordinate(s)
        return mgr
    else:
        # Create employee
        emp = Employee(name, salary)
        return emp


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 1:
        print('usage: testprog.py <json-input-file>')
        sys.exit(1)
    else:
        if os.path.exists(args[0]):
            # Load json employee data
            emp_data = []
            try:
                emp_data = json.loads(open(args[0], 'r').read())
            except json.JSONDecodeError as e:
                print('Failed to parse incoming json file: {}'.format(
                    e.msg
                ))
                sys.exit(1)

            # Create employee structures with input data
            employees = []
            for e in emp_data:
                employees.append(parse_employee(e))


            # Collect the salaries and hierarchy of all top-level employees
            total_salary = 0
            for e in employees:
                print(e.get_name())
                if type(e) == Manager:
                    e.report_hierarchy(1)
                total_salary += e.report_salaries()
            print('Total salary: {}'.format(total_salary))
            sys.exit(0)
        else:
            print('ERROR: Provided file \"{}\" does not exist in filesystem!'.format(args[0]))
            sys.exit(1)