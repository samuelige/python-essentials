import random

# Generate a random float between 0 and 1
random_float = random.random()
print(random_float)

# Generate a random integer
random.randint(1, 10)

# Generate random float
random.uniform(1, 5)

# Choose a random element from a list
my_list = ['apple', 'orange', 'banana', 'cherry']
random.choice(my_list)

# Shuffle a list
my_numbers = [1,2,3,4,5]
random.shuffle(my_numbers)

# Choosing multiple elements from a list aka sampling
random.sample(my_numbers, 3)