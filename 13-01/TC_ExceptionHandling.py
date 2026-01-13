try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("can't divide by zero")

try:
    x=int(input("Enter a number"))
    print(10/x)
except ValueError:
    print("Invalid entery")
except ZeroDivisionError:
    print("can't divide by zero")
else:
    print("Execution is successful")

