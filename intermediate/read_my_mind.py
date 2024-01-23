import random

# Generate a secret number
secret_number = random.randint(1, 100)
print(secret_number)

# Set your attempt
attempts = 5

# Accept user input


#Track attempt and  Provide hints
while attempts > 0:
    user_input = int(input("Guess number between 1 and 100: "))
    if(user_input < secret_number):
        print("Sorry, you guess is less than the secret number")
    elif(user_input == secret_number):
        print(f"Congratulations, you guessed right! The secret number is {secret_number}")
        break
    else:
        print("Sorry, you guess is greater than the secret number")
    attempts -= 1

