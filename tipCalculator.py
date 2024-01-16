# Challenge - Tip Calculator with Split Bill
# Your goal is to create a program that calculates the tip amount, the total cost of a meal at a restaurant, and the cost per
# person, based on the user's input.

# Prompt the user for the total cost of the meal.
totalMealCost = float(input("What is the total cost of your meal? "))
# Prompt the user for the tip percentage they would like to apply.
tipPercent = int(input("What is the tip percentage you would like to apply? (e.g. 5 for 5%) "))
# Prompt the user for the number of people at the table.
numberOfPeople = int(input("What is the number of people on your table? "))
# Calculate the tip amount using the tip percentage and the meal cost.
tipAmount = totalMealCost * (tipPercent / 100)
# Calculate the total cost of the meal, including the tip.
totalCost = totalMealCost + tipAmount
# Divide the total cost by the number of people at the table.
perPersonCost = totalCost / numberOfPeople
# Display the tip amount, total cost, and cost per person to the user.
print(f"Tip amount: {tipAmount:.2f}, total cost: {totalCost:.2f}, cost per person: {perPersonCost:.2f}")