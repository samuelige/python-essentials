# Functions

# Create a function to greet
def greet():
    print("Hello, Sammy!")

# Call the function
greet()

# Function with a parameter
def parameter(item):
    print(f"The {item} is delicious")

parameter("rice")

def mix_foods(food1, food2):
    return f"Mixing {food1} and {food2}"

party_dish = mix_foods("pizza", "tacos")
print(party_dish)

# Exercises
# 1. Create a function that adds numbers
def addNumbers(num1, num2):
    return num1 + num2

value = addNumbers(4,4)
print(value)

# 2. Count the number of vowels a word
def countVowels(word):
    words = word.lower()
    vowels = 'aeiou'
    counter = 0

    for word in words:
        if(word in vowels):
            counter += 1
    return counter


result = countVowels("samuel")
print(result)


# 3. Create a function that transforms Fahrenheit to celsius
def transformFahrenheit(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 0)

transform_result = transformFahrenheit(99)
print(transform_result)