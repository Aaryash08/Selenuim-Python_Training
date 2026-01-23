import json
import csv
import abc
class MarksDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError("Marks must be a list.")
        for mark in value:
            if not (0 <= mark <= 100):
                print("Invalid Marks\nError: Marks should be between 0 and 100")
                raise ValueError("Marks out of range")
        instance.__dict__[self.name] = value

class Person(abc.ABC):
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department

    @abc.abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        pass

class Student(Person):
    marks = MarksDescriptor("marks")

    def __init__(self, id, name, department, semester, marks):
        super().__init__(id, name, department)
        self.semester = semester
        self.marks = marks

    def get_details(self):
        print("Student Details:")
        print(f"Name      : {self.name}")
        print(f"Role      : Student")
        print(f"Department: {self.department}")

    def calculate_performance(self):
        if not self.marks:
            return 0, "F"
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "D" if avg>=60 else "E" if avg >= 50 else "F"
        return avg, grade

    def __gt__(self, other):
        if isinstance(other, Student):
            return (sum(self.marks) / len(self.marks)) > (sum(other.marks) / len(other.marks))
        return False

class Faculty(Person):
    def __init__(self, id, name, department, salary):
        super().__init__(id, name, department)
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    def get_details(self):
        print("Faculty Details:")
        print(f"Name      : {self.name}")
        print(f"Role      : Faculty")
        print(f"Department: {self.department}")

class Course:
    def __init__(self, code, name, credits, faculty_id):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty_id = faculty_id

    def __add__(self, other):
        if isinstance(other, Course):
            return self.credits + other.credits
        return 0


class CourseIterator:

    def __init__(self, courses):
        self._courses = courses
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._courses):
            result = self._courses[self._index]
            self._index += 1
            return result
        raise StopIteration

def student_generator(students):
    print("Student Record Generator\nFetching Student Records\n")
    for student in students:
        yield f"{student.id} - {student.name}"

class UniversitySystem:
    def __init__(self):
        self.students = []
        self.faculty = []
        self.courses = []
        self.enrollments = {}

    def add_student(self, student):
        if any(s.id == student.id for s in self.students):
            print("Error: Student ID already exists")
            return
        self.students.append(student)
        print("Student Created Successfully")
        print(f"ID        : {student.id}")
        print(f"Name      : {student.name}")
        print(f"Department: {student.department}")
        print(f"Semester  : {student.semester}")

    def add_faculty(self, faculty):
        self.faculty.append(faculty)
        print("Faculty Created Successfully")
        print(f"ID        : {faculty.id}")
        print(f"Name      : {faculty.name}")
        print(f"Department: {faculty.department}")

    def add_course(self, course):
        fac_name = next((f.name for f in self.faculty if f.id == course.faculty_id), "Unknown")
        self.courses.append(course)
        print("Course Added Successfully")
        print(f"Course Code : {course.code}")
        print(f"Course Name : {course.name}")
        print(f"Credits     : {course.credits}")
        print(f"Faculty     : {fac_name}")

    def enroll_student(self, student_id, course_code):
        student = next((s for s in self.students if s.id == student_id), None)
        course = next((c for c in self.courses if c.code == course_code), None)
        if student and course:
            self.enrollments[student_id] = course.name
            print("Enrollment Successful")
            print(f"Student Name : {student.name}")
            print(f"Course       : {course.name}")
        else:
            print("Error: Invalid Student ID or Course Code")

    def generate_report_csv(self):
        try:
            filename = 'students_report.csv'
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
                for s in self.students:
                    avg, grade = s.calculate_performance()
                    writer.writerow([s.id, s.name, s.department, f"{avg:.1f}", grade])
            print(f"CSV Report ({filename}) generated.")
        except IOError:
            print("Error: File access errors")

    def save_json(self):
        data = []
        for s in self.students:
            data.append({
                "id": s.id, "name": s.name, "department": s.department,
                "semester": s.semester, "marks": s.marks
            })
        try:
            with open('students.json', 'w') as f:
                json.dump(data, f)
            print("JSON Output Confirmation")
            print("Student data successfully saved to students.json")
        except IOError:
            print("Error: File not found or write permission denied")


def main():
    system = UniversitySystem()

    while True:
        print("\nSmart University Management System")
        print("1. Add Student")
        print("2. Add Faculty")
        print("3. Add Course")
        print("4. Enroll Student to Course")
        print("5. Calculate Student Performance")
        print("6. Compare Two Students")
        print("7. Generate Reports (CSV/JSON)")
        print("8. View All Students (Generator)")
        print("9. Exit")

        try:
            choice = input("Enter Choice: ")

            if choice == '1':
                sid = input("Student ID: ")
                name = input("Student Name: ")
                dept = input("Department: ")
                sem = int(input("Semester: "))
                marks = list(map(int, input("Marks (space separated): ").split()))
                try:
                    s = Student(sid, name, dept, sem, marks)
                    system.add_student(s)
                except ValueError:
                    pass

            elif choice == '2':
                fid = input("Faculty ID: ")
                name = input("Faculty Name: ")
                dept = input("Department: ")
                salary = float(input("Monthly Salary: "))
                f = Faculty(fid, name, dept, salary)
                system.add_faculty(f)

            elif choice == '3':
                code = input("Course Code: ")
                name = input("Course Name: ")
                credits = int(input("Credits: "))
                fid = input("Faculty ID: ")
                c = Course(code, name, credits, fid)
                system.add_course(c)

            elif choice == '4':
                sid = input("Student ID: ")
                ccode = input("Course Code: ")
                system.enroll_student(sid, ccode)

            elif choice == '5':
                sid = input("Enter Student ID: ")
                student = next((s for s in system.students if s.id == sid), None)
                if student:
                    avg, grade = student.calculate_performance()
                    print("Student Performance Report")
                    print(f"Student Name : {student.name}")
                    print(f"Marks        : {student.marks}")
                    print(f"Average      : {avg:.1f}")
                    print(f"Grade        : {grade}")

            elif choice == '6':
                id1 = input("Enter First Student ID: ")
                id2 = input("Enter Second Student ID: ")
                s1 = next((s for s in system.students if s.id == id1), None)
                s2 = next((s for s in system.students if s.id == id2), None)
                if s1 and s2:
                    print("Comparing Students Performance")
                    print(f"{s1.name} > {s2.name} : {s1 > s2}")

            elif choice == '7':
                system.generate_report_csv()
                system.save_json()

            elif choice == '8':
                gen = student_generator(system.students)
                for record in gen:
                    print(record)

            elif choice == '9':
                print("Thank you for using Smart University Management System")
                break

            else:
                print("Invalid Choice")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()