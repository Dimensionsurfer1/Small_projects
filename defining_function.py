# Write code below 💖
import random
possible_fortunes = ['Don\'t pursue happiness – create it.',
  'All things are difficult before they are easy.',
  'The early bird gets the worm, but the second mouse gets the cheese.',
  'Someone in your life needs a letter from you.',
  'Don\'t just think. Act!',
  'Your heart will skip a beat.',
  'The fortune you search for is in another cookie.',
  'Help! I\'m being held prisoner in a Chinese bakery!']
def fortune():
  the_random = random.randint(0,len(possible_fortunes))
  print('this is your fortune:')
  return possible_fortunes[the_random]  
participate = (input('do you want to know what i    s in your fortune cookie??, yes or no')).lower()
if participate == ('yes'):
  print(fortune())
elif participate == ('no'):
  print('oh! maybe next time :( ')
else:
  print('do you know how to answer?')
