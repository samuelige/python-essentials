# Sum of numbers
get_number = int(input("Enter a number: "))
range_number = range(1, get_number + 1)
print(sum(list(range_number)))

# or
total_sum = 0
for i in range(1, get_number + 1):
    total_sum += i

print(f"The is the iterated sum of the number provided - {total_sum}")