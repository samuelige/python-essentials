# Challence
# You are the bouncer at the entrance of Berghain nightclub. The club has the following rules for entry:
# Guests must be at least 18 years old.
# Guests must not be older than 60 years old.
# The maximum number of guests allowed in the club is 200.
# Using print and input functions, prompt the user for their age and the current number of guests inside the club. 
# Apply arithmetic operations and comparison operators to determine if the guest can enter the club.
# If the guest is allowed to enter, print a message saying, "Welcome to Berghain!"
# If the guest is not allowed to enter due to age restrictions, print a message saying, "Sorry, you cannot enter the
# club due to age restrictions."
# If the guest is not allowed to enter due to the club being at maximum capacity, print a message saying, "Sorry,
# the club is at maximum capacity. Please try again later."

# Solution

current_guest= 200
max_capacity = 200
min_age = 18
max_age = 60

# Using print and input functions, prompt the user for their age and the current number of guests inside the club. 
guest = int(input("How old are you?  "))

# Guests must be at least 18 years old.
if guest < min_age or guest >= max_age:
    print("Sorry, you cannot enter the club due to age restrictions.")
elif max_capacity >= current_guest:
    print("sorry, the club is at maximum capacity. Please try again later.")
else:
    print("Welcome to Berghain!")