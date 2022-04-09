# You are going to write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared.

# e.g. `4 * 4 = 16`
# e.g. `4 * 4 = 16`
# 4 squared equals 16.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
square_numbers = [num**2 for num in numbers]
print(square_numbers)

# You are going to write a List Comprehension to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [num for num in numbers if num % 2 ==0]
print(even_numbers)

# Take a look inside file1.txt and file2.txt. 
# They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which 
# contains the numbers that are common in both files.

data1 = open("./Day_26/file1.txt", mode="r")
file1 = data1.readlines()
print(file1)
data2 = open("./Day_26/file2.txt", mode="r")
file2 = data2.readlines()
print(file2)
result =[int(num) for num in file1 if num in file2 ]
print(result)