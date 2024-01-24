# Dictionaries

# Creating a dictionary
my_spellbook = {'fireball': 3, 'teleport': 5, 'heal': 2}
my_spellbook.items()

# Accessing the keys of the dictionary
my_spellbook.keys()

# Accessing the values of the dictionary
my_spellbook.values()

# Adding a key-value pair
my_spellbook['lightening'] = 4
print(my_spellbook)

# Updating a key-value pair
my_spellbook['heal'] = 3
print(my_spellbook)

# Deleting a key-value pair
del my_spellbook['lightening']
print(my_spellbook)