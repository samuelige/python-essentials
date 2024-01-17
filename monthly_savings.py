# Challenge:
# Your goal is to create a program that calculates the ideal monthly savings amount based on the user's age, target
# retirement age, desired savings amount at retirement, and an annual interest rate. To accomplish this, you will use
# Python operators and the following steps:
# Prompt the user for their current age.
# Prompt the user for their target retirement age.
# Prompt the user for their desired savings amount at retirement.
# Prompt the user for the annual interest rate on their savings.
# Calculate the number of years left until retirement.
# Calculate the total number of months left until retirement.
# Determine the ideal monthly savings amount based on the desired savings, the number of months left until
# retirement, and the interest rate.
# Display the ideal monthly savings amount to the user.

# Solution:

# Prompt the user for their current age.
current_age = int(input("Please enter your age? "))
# Prompt the user for their target retirement age.
retirement_age = int(input("Please enter your retirement age? "))
# Prompt the user for their desired savings amount at retirement.
desired_savings_amount = float(input("Please enter your desired savings amount? "))
# Prompt the user for the annual interest rate on their savings.
annual_interest_rate = float(input("Please enter your annual interest rate? "))
# Calculate the number of years left until retirement.
years_left_until_retirement = retirement_age - current_age
print(f"You have {years_left_until_retirement} years to work")
# Calculate the total number of months left until retirement.
months_left_until_retirement = years_left_until_retirement * 12
# Determine the ideal monthly savings amount based on the desired savings, the number of months left until retirement, and the interest rate.
monthly_interest_rate = (1 + annual_interest_rate / 100) ** (1/12) - 1 #This formula converts the annual interest rate to its equivalent monthly interest rate.

monthly_savings = (desired_savings_amount * monthly_interest_rate) / ((1 + monthly_interest_rate) ** months_left_until_retirement  -1) 
# Display the ideal monthly savings amount to the user.
print(f"Your ideal monthly savings amount: {monthly_savings:.0f}")