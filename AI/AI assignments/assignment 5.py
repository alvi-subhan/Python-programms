# Make an empty list for storing aliens.
aliens = []
from random import randint
x=randint(0,30)
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': x, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
