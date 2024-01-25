# Create a data structure for storing user's transactions, income, and expenses
transactions = []
income = {'salary': 0, 'investments': 0, 'other': 0}
expenses = {'groceries': 0, 'entertainment': 0, 'shopping': 0, 'other': 0}

# user input
while True:
    transaction_type = input("Is it an income or an expenses transaction?: ")
    if transaction_type == 'income':
        source = input("Enter the source (salary, investments, or other): ")
        amount = float(input("Enter the amount: "))
        income[source] += amount
        transactions.append(dict(transaction_type = transaction_type, source = source, amount = amount))
    elif transaction_type == 'expenses':
        categories = input("Enter the categories (groceries, entertainment, shopping, or other): ")
        amount = float(input("Enter the amount: "))
        income[categories] += amount
        transactions.append(dict(transaction_type = transaction_type, categories = categories, amount = amount))
    else:
        break

# Calculate total 
total_income = sum(income.values())
total_expenses = sum(expenses.values())
balance = total_income - total_expenses

# Print the into to the user
print("Transaction list: ")
print(transactions)
print(f"The total income is {total_income}")
print(f"The total expense is {total_expenses}")