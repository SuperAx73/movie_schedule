

current_movies={'The Grinch':'11:00am',
                 'Rudolph':'1:00pm',
                 'Frosty the snowman':'3:pm',
                 'Christmas Vacation':'5:00pm'}

print(f"We're currently showing the following movies:")

for key in current_movies:
    print(key)


movie=input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime == None:
    print("That movie isn't avalaible")
else:
    print(movie, 'is playing at' , showtime)