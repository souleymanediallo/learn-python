import datetime


class Employee:
    count_employee = 0
    amount_average = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + " " + last + "@google.com"
        Employee.count_employee += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def raise_average(self):
        salary = self.pay * self.amount_average
        self.pay += salary

    @classmethod
    def set_amount_average(cls, amount):
        Employee.amount_average = amount

    @classmethod
    def format_str(cls, text_str):
        first, last, pay = text_str.split
        return cls(first, last, pay)


    @staticmethod
    def is_working(day):
        if day.weekday == 5 or day.weekday == 6:
            return True
        return False


a = Employee("Ousmane", "Dieye", 78000)
e = Employee("Souleymane", "Diallo", 80000)

my_date = datetime.date(2021, 1, 8)

employe_1 = "Abou-DIA-55000"

print(Employee.amount_average)
Employee.set_amount_average(1.08)
print(Employee.amount_average)

print(Employee.is_working(my_date))
print(help(Employee))
