# Simple list
numbers = [1,2,3,4,5]

# Mixed list
mixed_list = [42, "Hello", 3.14, True]

# Accessing the list
# Get by index
print(numbers[0])

# Slicing - Grabbing a portion of the list
print(numbers[1:3])

# Modifing 
numbers[0] = 100
print(numbers)

# Adding items to the list
# Append method
numbers.append(9)

# Concatenate with the +
numbers = numbers + [10, 23, 43]
print(numbers)

