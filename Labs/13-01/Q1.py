from functools import reduce
# range()
for i in range(1,20):
    print(i)

numbers = [1, 2, 3, 4, 5]
# filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# map()
squares = list(map(lambda x: x**2, even_numbers))
print(squares)
# reduce()
Total = reduce(lambda a, b: a + b, squares)
print(Total)
# enumerate()
for index, value in enumerate(squares):
    print(f"Index: {index}, Value: {value}")
