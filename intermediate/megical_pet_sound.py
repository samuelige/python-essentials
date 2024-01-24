# Magical pet sound dictionary
pet_sounds = {'mew': 'I am hungry', 
              'woof': 'I want to play', 
              'grr': 'I am angry'}

# Create a Python code that tells the user the meaning of the sound

# Solution
sound = input("Enter a sound: ")
if(sound in pet_sounds):
    print(pet_sounds[sound])
else:
    print("Not found")

