class PositiveSalary:
    def __get__(self, instance, owner):
        return instance._salary
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        instance._salary = value
class Employee:
    salary = PositiveSalary()
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)
try:
    emp3 = Employee("Charlie", -45000)
except ValueError as e:
    print("Error:", e)
