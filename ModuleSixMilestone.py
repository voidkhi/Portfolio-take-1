#Taylor Yager

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }
#Set the starting room to the great hall
starting_room = 'Great Hall'

#Set the current room to the starting room
current_room = starting_room

while True:
    #Print current room for user
    print('\nYou are currently in {}'.format(current_room))

    #Prompt the user to enter a command and provide instructions
    move = input('You can enter South, North, East, or West to move. Enter Exit to win the game.\nEnter your move:').split()[-1].capitalize()

    #if user types exit, then exit the game
    if move == 'Exit':
        current_room = 'exit'
        print('Thanks for playing, bye!')
        break
    #if user types a valid command
    elif move in rooms[current_room]:
        current_room = rooms[current_room][move]

    #if user types an invalid command
    else:
        print("You can't go that way!".format(move))

