#Taylor Yager

import sys

#instructions function
def print_instructions():
    print('***********************************************************************************************')
    print('You wake to the strong smell of burning hair and the feel of electricity in the air.\nA man with large goggles, unkempt hair, and rubber gloves is shouting, loudly, "My creature, it lives!".' )
    print('The strange man removes your bindings. "Walk for me my creation!", he says. You walk uneasily towards him.')
    print('"Yes! Yes my creature, yes!", he shouts. "However, I am sure we can optimize you further.\nYes. I must not install your final power source until you are perfect, my lovely."')
    print('The strange man heads east and exits the room, leaving you standing there alone.')
    print('***********************************************************************************************')
    print('A few moments later a bat drops from the ceiling. Flying in front of your face it says:')
    print('***********************************************************************************************')
    print('Look, that guy is super creepy. A real weirdo. He has done this dozens of times before and it never ends well\nfor his "creations". Frankly, I am tired of watching it happen. It is depressing.')
    print('In order to get out of here you need 8 items:\nA power source to boost your energy production, shoes, money, a snack, a flashlight,\ntoothpaste and a toothbrush (your breathe is awful), a teddy bear (everyone needs a friend and it is dangerous to go alone),\nand the master key.')
    print('A word of warning. That guy is probably in the conservatory. If he sees you out and about, he will dismantle you.\nAlso if you leave without all of the items, you will probably be caught by the angry mob that roams outside of this place.')
    print('Good luck friend!')
    print('***********************************************************************************************')

def get_items(): #a function to allow the user to add 'items' from inside the dictionary into their inventory
    if ('items' in rooms[current_room]) and (rooms[current_room]['items'] not in inventory):  # if there exists an 'item' or 'items' in the room, that do not exist in the inventory
        pick_up = (rooms[current_room]['items'])  # Assign those items to a variable
        # pick_up = rooms[current_room]['item']
        print('You also see:', pick_up)  # print those items for the user to see
        add_item = input('Add the item(s) to your inventory? Y/N:').capitalize()  # prompt for response
        if add_item == 'Y':  # if the user types Y, then add the item to the inventory and print that the item has been added
            inventory.append(pick_up)
            print('The item(s) have been added to your inventory. You have:', inventory)
        while add_item != ('Y' or 'N'):  # invalid command, advise user and move on. item remains in room
            print("Invalid Command! Try a different one.".format(move))
            print('You also see:', pick_up)  # print those items for the user to see
            add_item = input('Add the item(s) to your inventory? Y/N:').capitalize()  # prompt for response
            if add_item == 'Y':  # if the user types Y, then add the item to the inventory and print that the item has been added
                inventory.append(pick_up)
                print('The item(s) have been added to your inventory. You have:', inventory)


#A dictionary for the game
#The dictionary links a room to other rooms. It also contains items.
rooms = {
	'Laboratory': {'East': 'Kitchen', 'South': 'Bedroom'},
	'Kitchen': {'North': 'Conservatory',  'East': 'Bouncy House Room', 'West': 'Laboratory', 'item': 'Snack', 'items': 'Master Key'},
	'Bedroom': {'North': 'Laboratory', 'South': 'Bathroom', 'item': 'Teddy Bear dressed as a doctor'},
	'Bathroom': {'North': 'Bedroom', 'East': 'Theatre', 'item': 'Toothpaste and Toothbrush'},
	'Bouncy House Room': {'West': 'Theatre', 'item': 'Shoes'},
	'Theatre' : {'South': 'Backstage', 'West': 'Bathroom','item': 'Clothes', 'items' : 'Money'},
	'Backstage': {'North': 'Theatre','item': 'Flashlight', 'items' : 'Power Source'}

}

inventory = [] #inventory where the items will be stored

#Set the starting room to the great hall
starting_room = 'Laboratory'

#Set the current room to the starting room
current_room = starting_room

print_instructions() #call to print instructions function

while True: #Initiate loop
    #Print current room for user
    print('\nYou are currently in the {}'.format(current_room))
    print('You have found:', inventory) #Print inventory contents

    #Prompt the user to enter a command and provide instructions
    move = input('You can enter South, North, East, or West to move.\nEnter your move:').capitalize()

    #if user types exit, then exit the game
  #  if move == 'Exit':
   #     current_room = 'exit'
    #    print('Thanks for playing, bye!')
     #   break
    #if user types a valid move command
    if move in rooms[current_room]: #movement
        current_room = rooms[current_room][move]
        if current_room == 'Kitchen': #Kitchen specific description
            print('***********************************************************************************************')
            print('You enter the Kitchen furnished with only a small stove, a fridge, and a table. There are no chairs or windows. On the table')
            get_items()

        if current_room == 'Bouncy House Room': #bouncy house specific description
            print('***********************************************************************************************')
            print('You open the door to see an entire room filled by a giant bouncy house. It smells faintly of solvents and play dough.\nYou spend a lot of time bouncing in the room. As you calm down and make your way through')

        if current_room == 'Theatre': #Theatre specific description
            print('***********************************************************************************************')
            print('You are behind several rows of cheap folding chairs all filled with human shaped cardboard cutouts.\nThe chairs face a stage. The set is a scale replica of a starbucks, with a cutout as a cashier.\nIn lieu of a menu, there is a large sign that says "Practice Humiliation.". Making your way onto the stage')
            get_items()

        if current_room == 'Bedroom': #Bedroom specific description
            print('***********************************************************************************************')
            print('Stepping forward, you enter the bedroom. The bedframe, lamp, table and chair are all metal.\nAny soft material (cushions, blankets, etc.) are sealed in plastic. The wallpaper is peeling,\nthere are stains on the concrete floor and no windows. On the bed')

        if current_room == 'Bathroom': #Bathroom specific description
            print('***********************************************************************************************')
            print('You enter a surprisingly normal looking bathroom. Linoleum covers the ground, the walls are painted an austere white. On the sink')

        if current_room == 'Conservatory': #Conservatory specific description and the game has been lost scenario 1
            print('***********************************************************************************************')
            print('You enter a large spherical glass room full of servers, cables, monitors, and other items of a techniological nature.\nThe strange man from the Laboratory is hunched over a monitor furiously typing away.')
            print('Startled, he looks up and sees you."What on earth are you doing here my dearest?! Oh this will not do, this will not do at all.\nI cannot have a creation who wanders about aimlessly. We do not tolerate inefficiencies in this house my love!"')
            print('I am afraid you must come with me." He grabs your wrist and leads you back to the lab where you are dismantled.\nThe bat hanging from the Laboratory ceiling shakes its head. "Maybe the next one will get away..." he says with a sigh.')
            print('You Loose, try again.')
            sys.exit() #handy command that exits the game after a loss

        if current_room == 'Backstage': #Backstage specific description and options
            print('***********************************************************************************************')
            print('While on the stage you see a realistic looking door labeled "Managers Office". You open this door to find that you are now backstage. You see a door marked exit.')

            get_items()

            leave = input('If you have the key, and wish to leave, type "Exit". Otherwise type anything else.').capitalize()#present the user with the option of leaving
            if (leave == 'Exit') and ('Snack and Master Key' in inventory) and (len(inventory) == 8):#if exit is typed and the conditions are met, then this options executes and the user wins the game
                print('***********************************************************************************************')
                print('The door opens with a squeak. Cool air and dark sky greet you as you step outside. You insert your power source into your chest, put on your shoes, and light your flashlight.\nYou are able to run and avoid the xenophobic mob marching around the house.\n"Congratulations" squeaks the bat from the Laboratory! You have escaped! Follow me and I will take you to a safe place.')
                print('***********************************************************************************************')
                print('Thanks for playing the game, hope you enjoyed it!')
                sys.exit()
            if (leave == 'Exit') and ('Snack and Master Key' in inventory) and (len(inventory) != 8):#if exit is typed and the conditions are met, then this options executes and the user looses the game
                print('***********************************************************************************************')
                print('The door opens with a squeak. Cool air and dark sky greet you as you step outside. You hear footsteps and angry shouts as a xenophobic mob approaches you.\nYou attempt to hobble away and escape but are unsuccessfull. The mob captures you and you are never seen from again.')
                print('The bat in hanging from the Laboratory ceiling shakes its head. "Maybe the next one will get away..." he says with a sigh.')
                print('You Loose, try again.')
                sys.exit()

            else:#loop continues until user attempts to exit
                continue

    #if user types an invalid command
    else:
        print("Invalid Command! Try a different one.".format(move))
        continue

    # show user items and prompt them to pick them up
    if ('item' in rooms[current_room]) and (rooms[current_room]['item'] not in inventory):#if there exists an 'item' or 'items' in the room, that do not exist in the inventory
        pick_up = rooms[current_room]['item'] #Assign those items to a variable
       # pick_up = rooms[current_room]['item']
        print('You also see:', pick_up)#print those items for the user to see
        add_item = input('Add the item(s) to your inventory? Y/N:').capitalize()#prompt for response
        if add_item == 'Y':#if the user types Y, then add the item to the inventory and print that the item has been added
            inventory.append(pick_up)
            print('The item(s) have been added to your inventory. You have:', inventory)
        while add_item != ('Y' or 'N'):  # invalid command, advise user and move on. item remains in room
            print("Invalid Command! Try a different one.".format(move))
            print('You also see:', pick_up)  # print those items for the user to see
            add_item = input('Add the item(s) to your inventory? Y/N:').capitalize()  # prompt for response
            if add_item == 'Y':  # if the user types Y, then add the item to the inventory and print that the item has been added
                inventory.append(pick_up)
                print('The item(s) have been added to your inventory. You have:', inventory)












