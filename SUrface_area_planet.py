from math import pi
from random import choice as ch
planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]
random_planet = ch(planets)
if random_planet is 'Mercury':
  r = 2440.
elif random_planet is 'Venus':
  r = 6052.
elif random_planet is 'Earth' :
  r = 6371.
elif random_planet is 'Mars':
  r = 3390.
elif random_planet is 'Saturn':
  r = 58232.
else:
  print ("Oops! An error occurred.")
planet_area = round(4 * pi * r * r)
print(f'the planet {random_planet} covers a surface area of {planet_area} Km')
