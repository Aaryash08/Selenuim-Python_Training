from abc import ABC, abstractmethod
import time
import json
import csv

class Person(ABC):
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        print(f"[LOG] {self.name} object destroyed")
class MarksDescriptor:
    def __set__(self, instance, value):
        if any(m < 0 or m > 100 for m in value):
            raise ValueError("Error: Marks should be between 0 and 100")
        instance.__dict__['marks'] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get('marks')
class SalaryDescriptor:
    def __get__(self, instance, owner):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, instance, value):
        instance.__dict__['_salary'] = value
class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, dept, semester, marks):
        super().__init__(sid, name, dept)
        self.semester = semester
        self.marks = marks

    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B"
        return avg, grade

    def get_details(self):
        print("Student Details:")
        print("--------------------------------")
        print("Name      :", self.name)
        print("Role      : Student")
        print("Department:", self.department)

    def __gt__(self, other):
        return self.calculate_performance()[0] > other.calculate_performance()[0]
class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, dept, salary):
        super().__init__(fid, name, dept)
        self.salary = salary

    def get_details(self):
        print("Faculty Details:")
        print("--------------------------------")
        print("Name      :", self.name)
        print("Role      : Faculty")
        print("Department:", self.department)
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits

def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper

def admin_only(func):
    def wrapper(*args, **kwargs):
        print("Access Denied: Admin privileges required")
    return wrapper
def student_generator(students):
    print("Fetching Student Records...")
    print("--------------------------------")
    for s in students:
        yield f"{s.pid} - {s.name}"


def save_students_json(students):
    data = []
    for s in students:
        avg, grade = s.calculate_performance()
        data.append({
            "id": s.pid,
            "name": s.name,
            "department": s.department,
            "average": avg,
            "grade": grade
        })

    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Student data successfully saved to students.json")


def generate_csv_report(students):
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])

        for s in students:
            avg, grade = s.calculate_performance()
            writer.writerow([s.pid, s.name, s.department, avg, grade])
# Creating objects
s1 = Student("S101", "Aaryash Kumar", "Computer Science", 8, [78,85,90,88,92,92,87,79])
s2 = Student("S102", "Shashank Kumar", "Computer Science", 8, [70,75,80,72,78,86,82,77])

f1 = Faculty("F201", "Dr. Kumar", "Computer Science", 85000)

c1 = Course("CS401", "Data Structures", 4, f1)
c2 = Course("CS402", "Algorithms", 3, f1)

# Polymorphism
s1.get_details()
f1.get_details()

# Performance
avg, grade = s1.calculate_performance()
print("Average:", avg, "Grade:", grade)

# Operator Overloading
print("Compare Two Students (> operator)")
print(s1.name, ">", s2.name, ":", s1 > s2)

print("Total Credits After Merge :", c1 + c2)

# Generator
for record in student_generator([s1, s2]):
    print(record)

# File Output
save_students_json([s1, s2])
generate_csv_report([s1, s2])

print("Thank you for using Smart University Management System")
