import time


class employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        print(f"Monthly Salary : {self.monthly_salary}")
        print(f"Annual Salary : {12*self.monthly_salary}")

    def give_raise(self, percentage):
        new_monthly_salary = int(
            ((self.monthly_salary / 100) * percentage) + self.monthly_salary
        )
        print(f"Raise in salary {percentage}%.")
        print(f"After raise Monthly Salary : {new_monthly_salary}")
        print(f"Annual Salary : {12*new_monthly_salary}")


# e1 = employee("Atta", 170000)
# e1.annual_salary()
# e1.give_raise(10)
