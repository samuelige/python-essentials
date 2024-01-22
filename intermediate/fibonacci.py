# Print the first 10 Fibonacci numbers
first_number = 1
second_number = 1

fibonacci = []

while len(fibonacci) < 10:
    fibonacci.append(first_number)
    third_number = first_number + second_number
    first_number = second_number
    second_number = third_number
    print(fibonacci)

