import random
# Random Movie Picker: 
#Create a list of your favorite movies
#write a program that randomly picks a movie to watch until you've seen them all.
favorites_movies = []
remaining_movies = ['The Matrix', 'Inception', 'The Dark Knight', 
                    'Avengers: Endgame', 'Interstellar']
counter = 0
while counter < len(remaining_movies):
    select_movie = random.choice(remaining_movies)
    counter += 1
    if favorites_movies.__contains__(select_movie):
        continue
    else:
        favorites_movies.append(select_movie)
         
print(favorites_movies)

