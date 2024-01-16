# Challenge: Can you vote
# Create a if-else condition that tells you whether they can vote 
# The assessemnt must be based on their age

user = input("Please enter your name: ")
age = int(input("Please enter your your age: (Note that you must be above 18 to be able to vote) "))

if(age >= 18): 
    print(f"Congratulations {user}, you're eligible to vote.")
elif age > 16 and age < 18:
    print(f"We're sorry {user}, you're not eligible to vote this year. Please try again next year.")
else: 
    print(f"We're sorry {user}, you're not eligible to vote.")