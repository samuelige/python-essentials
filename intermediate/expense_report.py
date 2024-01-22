# Exercise - Monthly Expense Report 

# Monthly report of expenses
# Compute the total expense for the month
# Compute the average spending for the month

#Expense report
monthly_expenses = [1200, 1350, 1050, 1450, 1150, 900, 1220]

# Total expense
total_expense = sum(monthly_expenses)

# Average spending
average_spend = total_expense / len(monthly_expenses)

print(f"{average_spend:.0f}")