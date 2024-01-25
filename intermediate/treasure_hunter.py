# Game data
locations = {
    'start': {
        'description': "You are at the starting point. There are two paths: left and right.",
        'options': {'left': 'forest', 'right': 'cave'}
    },
    'forest': {
        'description': "You are in a dense forest. There are two paths: forward and backward.",
        'options': {'forward': 'river', 'backward': 'start'}
    },
    'cave': {
        'description': "You are inside a dark cave. There are two paths: forward and backward.",
        'options': {'forward': 'treasure', 'backward': 'start'}
    },
    'river': {
        'description': "You are at the edge of a roaring river. There is no way forward.",
        'options': {'backward': 'forest'}
    },
    'treasure': {
        'description': "You've found the treasure! Congratulations!",
        'options': {}
    }
}

# user_input = "start"
user_input = input("Enter your current location e.g. start, forest, cave, river etc ")
while True:
    if(user_input in locations):
        # user's location description
        locations_description = locations[user_input]['description']
        print(f"location description: {locations_description}")
        # user's location options
        location_options = locations[user_input]['options']
        for option in location_options:
            print(f"-: {option}")
        user_option_choice = input("Choose an option ").lower()
        if(user_option_choice not in location_options):
            user_option_choice = input("Invalid option. Choose again ").lower()
        else:
            print(f"-: {user_option_choice}")
            # Update the value of location
            user_input = location_options[user_option_choice]

        if user_input == 'treasure':
            print("Gave over! You found the treasure")
            break
    else:
        break
