# Write code below 💖
import random 
symbols = ['🍒',' 🍇', '🍉', '7️⃣']
i = 1
def play():
  start_machine = str(input('would you like to play the game? y or n'))
  return start_machine
play = play() 
while play == 'y':
  print(f'spin no: {i} ')
  result = random.choices(symbols,k=3)
  if result == ['7️⃣','7️⃣','7️⃣']:
    print('Jackpot! 💰') 
  else:
    print('Thanks for playing, better luck next time')
  play = (input('do you want to play again? y or n')) 
print('see you next time')