   # Ingredient list
ingredients = [
    {'name': 'flour', 'quantity': 200, 'unit': 'g'},
    {'name': 'sugar', 'quantity': 100, 'unit': 'g'},
    {'name': 'butter', 'quantity': 150, 'unit': 'g'},
    {'name': 'eggs', 'quantity': 2, 'unit': 'pcs'},
    {'name': 'vanilla extract', 'quantity': 5, 'unit': 'ml'}
]

# Conversion table
conversion_table = {
    'g': {'oz': 0.035274, 'cups': 0.00422675, 'tbsp': 0.067628, 'tsp': 0.202884},
    'oz': {'g': 28.3495, 'cups': 0.119826, 'tbsp': 1.91722, 'tsp': 5.75167},
    'cups': {'g': 236.588, 'oz': 8.3454, 'tbsp': 16, 'tsp': 48},
    'tbsp': {'g': 14.7868, 'oz': 0.521594, 'cups': 0.0625, 'tsp': 3},
    'tsp': {'g': 4.92892, 'oz': 0.173473, 'cups': 0.0208333, 'tbsp': 0.333333}
}