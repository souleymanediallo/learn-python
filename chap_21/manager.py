from chap_21.app import Employee


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def move_employee(self, employee):
        if employee in self.employees:
            self.employees.removed(employee)

    def print_employees(self):
        for employee in self.employees:
            print("--->", employee.fullname())
