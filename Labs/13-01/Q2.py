data=[1,2,3,4,5,6,2,4]
# List
Squares=[x**2 for x in data]
print(Squares)
# Set
even_set={x for x in data if x%2==0}
print(even_set)
# Dictionary
cube_dict={x:x**3 for x in data}
print(cube_dict)