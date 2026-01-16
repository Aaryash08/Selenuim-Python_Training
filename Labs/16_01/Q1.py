class student():
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print(self.name,self.rollno)

s1=student("Ravi",1)
s1.display()
s2=student("Ram",2)
s2.display()