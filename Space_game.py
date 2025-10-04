start_the_game = int(input('do you want to play a game? for yes type 1, for no type 0: '))
adventures = 0
if start_the_game == 1:
    print('let\'s play!')
    adventures += 1 
elif start_the_game == 0:
    print('ok, maybe next time!')
    exit()
print('let\'s start your adventure!')
if adventures == 1:
    print('''You are Commander Aris Veynn, tasked with leading the first expedition through the Veil.
Your fleet of three ships is caught in anomalies near the mining colony Erevos-9. Each ship is trapped in a different danger, and you must solve puzzles to free them.
Fail, and the ships will be lost forever in the void.''')
    print('Your scout ship “Nova’s Edge” is pulled into a gravity well. To stabilize, you must balance the thrusters.')
    print('to balance the thrusters solve the equation: 3x + 5 = 20. what is x?')
    x = int(input('type your answer here: '))
    if x == 5:
        print('correct! the thrusters are balanced, and the ship is free!')
        print('your adventure continues...')
        adventures += 1
        pass
    while x != 5:
        print('incorrect! the ship is lost in the gravity well forever. game over.')
        print('try again?')
if adventures == 2:
    print('your ship is cought in a trap of void trap by XOLCA the pirate king of space, to escape and shoot at him you must solve his riddle:')
    print('I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind. What am I?')
    riddle_answer = input('type your answer here: ').lower()    
    if riddle_answer == 'echo':
        print('ahhhh!!! what a discusting rocket this time you escaped but next time you are dead')
        adventures += 1
    while riddle_answer != 'echo':
        print('hahahaha you dombo you are of no good, PEW PEW PEW you are dead')
        print('try again?')
        exit()
if adventures == 3:
    print('this was your last adventure, you have done amazing job commander hope we meet you again')
    exit()
