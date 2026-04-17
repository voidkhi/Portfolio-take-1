#Taylor Yager

import sys #import handy built ins

#instructions function
def print_instructions():
    print('***********************************************************************************************')
    print('We awake to the smell of ozone burning our sinuses, the sensation blossoms through our skull like a battery threw up in us and sparked an electrical fire.\nA man with large goggles, unkempt hair, and rubber gloves is shouting, loudly, "My creature, it lives!".' )
    print('The strange man removes our bindings. "Walk for me my creation!", he says. We walk uneasily towards him.')
    print('"Yes! Yes my creature, yes!", he shouts. "However, I am sure we can optimize you further.\nYes. I must not install your final power source until you are perfect, my lovely."')
    print('The strange man heads east and exits the room, leaving us alone.')
    print('***********************************************************************************************')
    print('A few moments later a bat drops from the ceiling. Flying in front of our face it says:')
    print('***********************************************************************************************')
    print('Look, that guy is super creepy. A real weirdo. He has done this dozens of times before and it never ends well\nfor his "creations". Frankly, I am tired of watching it happen.')
    print('In order to get out of here you need 8 items:\nA power source to boost your energy production,\nshoes,\nmoney,\na snack,\na flashlight,\ntoothpaste and a toothbrush (your breathe is awful),\na teddy bear (everyone needs a friend),\nand the master key.')
    print('A word of warning. That guy is probably in the conservatory. If he sees you out and about, he will dismantle you.\nAlso if you leave without all of the items, you will probably be caught by the angry mob that roams outside of this place.')
    print('Good luck friend!')
    print('***********************************************************************************************')

def get_items(): #a function to allow the user to add 'items' from inside the dictionary into their inventory
    if ('items' in rooms[current_room]) and (rooms[current_room]['items'] not in inventory):  # if there exists 'items' in the room, that do not exist in the inventory
        pick_up = (rooms[current_room]['items'])  # Assign those items to a variable
        print('You also see:', pick_up)  # print those items for the user to see
        add_item = input('Add the item(s) to your inventory? Y/N:').capitalize()  # prompt for response

        if add_item == 'Y':  # if the user types Y, then add the item to the inventory and print that the item has been added
            inventory.append(pick_up)
            print('The item(s) have been added to your inventory. You have:', inventory)

        while (add_item != 'Y') and (add_item != 'N'):  # invalid command, advise user and move on. item remains in room
            print("Invalid Command! Try a different one.".format(move))
            print('You also see:', pick_up)  # print those items for the user to see
            add_item = input('Add the item(s) to your inventory? Y/N:').capitalize()  # prompt for response

            if add_item == 'Y':  # if the user types Y, then add the item to the inventory and print that the item has been added
                    inventory.append(pick_up)
                    print('The item(s) have been added to your inventory. You have:', inventory)
            if add_item == ('N' or 'n'):  # if the user types N, exit the loop
                    break


def get_item(): #a function to allow the user to add 'item' from inside the dictionary into their inventory
    if ('item' in rooms[current_room]) and (rooms[current_room]['item'] not in inventory):  # if there exists an 'item' in the room, that does not exist in the inventory
        pick_up = (rooms[current_room]['item'])  # Assign those items to a variable
        print('You also see:', pick_up)  # print those items for the user to see
        add_item = input('Add the item(s) to your inventory? Y/N:').capitalize()  # prompt for response

        if add_item == 'Y':  # if the user types Y, then add the item to the inventory and print that the item has been added
            inventory.append(pick_up)
            print('The item(s) have been added to your inventory. You have:', inventory)

        while (add_item != 'Y') and (add_item != 'N'):  # invalid command, advise user and move on. item remains in room
            print("Invalid Command! Try a different one.".format(move))
            print('You also see:', pick_up)  # print those items for the user to see
            add_item = input('Add the item(s) to your inventory? Y/N:').capitalize()  # prompt for response

            if add_item == 'Y':  # if the user types Y, then add the item to the inventory and print that the item has been added
                    inventory.append(pick_up)
                    print('The item(s) have been added to your inventory. You have:', inventory)
            if add_item == ('N' or 'n'):  # if the user types N, then exit loop
                    break


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

inventory = [] #inventory where the items gathered by the user will be stored

#Set the starting room to the Laboratory
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

    #if user types a valid move command
    if move in rooms[current_room]: #movement
        current_room = rooms[current_room][move]

        if current_room == 'Kitchen': #Kitchen specific description
            print('***********************************************************************************************')
            print("A kitchen, we think of the smell of spaghettios but don't recall what they are but are certain")
            print("there are none here.  The formica countertops have faded to sallow gritty planks. Dustballs. The")
            print("stove, its elements corroded and caked in black. We think of a basement, the grit of concrete")
            print("underneath our bare skin, the porous cold of it. We look at our feet and the thought ends. A")
            print("refrigerator with a latch, the enamel an off white the handle a shinny chrome now dulled by dust,")
            print("we hear the click it would make if we pulled on it, the metallic crunch of the mechanism giving way,")
            print("but we keep our hands to ourselves like good children. We feel an intense pain in our forearm")
            print("feel the skin char and bubble away from something we can't see. We look at our forearm, where we")
            print("remember a twisted and puckered mound of plasticy purple flesh we see only skin,smooth and unmolested")
            print("by trauma. Good boys don't touch the fridge she says from the shadows, her shakes have taken her again.")
            print("We smell her sweat, her soiled clothes. The table is olive green and holds only dust atop it, we give")
            print("pause to the long spindly metal legs but find no reason why. No chairs under the table. No window")
            print("above the sink that looks out to the corn field. No light fixture above. No food in the cupboards")
            print("that hang from what twisted hinges remain. We are more bothered by what isn't.")
            get_items() #function call to get 'items'

        if current_room == 'Bouncy House Room': #bouncy house specific description
            print('***********************************************************************************************')
            print("You open the door to a great room occupied by a giant rainbow bouncy house. It smells faintly of")
            print("solvent and play dough. We spend a lot of time bouncing. We smell birthday cake. See its pastel frosting")
            print("blue and pink, the waved edges of its piping, purple. He slaps the back of our head for putting our finger")
            print("in it and our vision goes blurry. We cry and he yells. It's our cake, why can't we have a taste now?  Mom")
            print("number three smokes at the table. She absently touches her eye swollen and purple, pink like the cake, her")
            print("hand shakes and she forces herself to place it flat on the olive green table. Shaving cream in our mouth")
            print("like soap we can't spit out. The grass gives us hives and dad smiles and holds our hand in his so big and")
            print("rough as he dabs the pink medicine on our rash. It feels cool, the swell of relief is better than any cake.")
            print("There there, the itch will stop and then we can have cake!  The cake tastes of our metallic spit from where")
            print("she slapped us for peeking. The split in our lip burns so we don't smile. If Heather would come to our party,\nit would all be worth it, she didn't RSVP but we're sure she'll be here, she said so in fourth period. After we calm down we make our way through")

        if current_room == 'Theatre': #Theatre specific description
            print('***********************************************************************************************')
            print("An audience of empty chairs smiles in a crescent before a stage. A theater, here? 'That ain't no fuckin metaphor'")
            print("coach Guillimon spits with contempt. 'A fifteen minute fuckin mile ain't funny. If y'all want equal rights then run equal times.")
            print("No, it's an array of empty chairs for some absent audience. Drama Club without the rigging overhead. What is a key grip, I'll")
            print("tell you Mr. Shadik says to us on day one. The dance recital we got to too late, the bar was right there, we were early, we only")
            print("had a few. She'll understand this time we tell ourselves as we wipe the cold sweat from our brow with our tie now loose about our")
            print("neck. We make our way through to the stage, the flat silhouettes of cardboard people rotate into existence as we walk past them")
            print("then rotate back into thin lines lost in the dimness of the auditorium. We feel what we can't see now that we know. The stage is")
            print("a coffeeshop fresh from 13th street. Or Main and 5th. Just like the one in Naples from our senior trip. The one off Pine St we'd")
            print("run to at lunch or Silverton and Cassowary with the cute barista before work.  But still and empty like the M when we'd be at 5am")
            print("opening during our first year of college, the sounds of opening prep work, just us before the sun. Zero hour, never again. Bianca")
            print("tells us we're just friends, she got the scholarship to study abroad in Hong Kong next semester, as she scrolls through her phone")
            print("and tells us she doesn't have time to be romantically involved, we swallow the lump in our throat and say 'yeah, we're friends' and")
            print("look away so she can't look us in the eyes when she hears us lie. We sip our bitter cold coffee.")
            print("We look up to the menu.  There are no prices. No items. Only the words 'Practice Humiliation' black in a background of white.")
            get_items() #function call to get 'items'

        if current_room == 'Bedroom': #Bedroom specific description
            print('***********************************************************************************************')
            print("A bedroom. Only without the comforts that define a bedroom. A bedframe with no mattress. A lamp")
            print("with no lightbulb. A table slumped against the wall, it's fourth leg parallel to the ground beneath it.")
            print("The wallpaper peels back from the wall as skin curls back from bone in a furnace as it crumbles to ash,")
            print("wreathed in flame.  Woah. What? Mrs. Beecherly smoked for decades, her cigarettes, their tar and nicotine,")
            print("seemed to mummify her without the promise of eternity. Mom, we say, mom, they're going to have to cut a ")
            print("hole in your trachea and install a plug. She takes a pull of her cigarette, its end glows red like her hair")
            print("in the sun of her childhood, now grey and thin. Her eyes cold as perfection. We long for a warmth not of")
            print("this room with a bed and no bedding, no pillows, only the stained concrete of the floor, the harsh metal")
            print("edges of the frame, the failure evidenced by the table collapsed in entropy. When the sun rises, we'll be")
            print("able to see again, your sister tells us as she looks to the high barred window overhead now black.\nThey only come at night. There is no window here.")

        if current_room == 'Bathroom': #Bathroom specific description
            print('***********************************************************************************************')
            print("A bathroom. Where one paradoxically defecates and bathes in the same immediate space. This one smells")
            print("like... play dough.  We feel a sensation in our anatomy not felt since 3rd year summer camp, the one we")
            print("don't tell our friends about when we've had too much to drink because then--just like Sally Winkle--they'll")
            print("never talk to us again and give us horrified looks when they see us at parties and promptly leave. No amount")
            print("of Smashmouth can deafen their visible judgement. Save our sensation for someone special that we'll meet later")
            print("in life, like our therapist or priest--if we ever trust one again. Anyway. Who is Sally Winkle and what is")
            print("Summer Camp? What the hell is a smashmouth?  In the tub is a rainbow of putty not yet mixed to the color of")
            print("desaturated brown, empty soup cans with the words 'plae dou' scrawled on them liter the linoleum, they rattle")
            print("and clink about our intruding footsteps. Is that... mold? Nacho cheese mold? In the sink? It contrasts with")
            print("the clinical white of the painted stucco walls. We think faintly of Panther Bodied Crown Victorias, a breeze")
            print("on a July night so late it's almost morning, a stain we can't explain in our book bag, Jansport, Converse, we")
            print("don't understand why any of it is important. Or seemingly, now, not.")

        if current_room == 'Conservatory': #Conservatory specific description and the game has been lost scenario 1
            print('***********************************************************************************************')
            print('You enter a large spherical glass room full of servers, cables, monitors, and other items of a techniological nature.\nThe strange man from the Laboratory is hunched over a monitor furiously typing away.')
            print('Startled, he looks up and sees you."What on earth are you doing here my dearest?! Oh this will not do, this will not do at all.\nI cannot have a creation who wanders about aimlessly. We do not tolerate inefficiencies in this house my love!"')
            print('I am afraid you must come with me." He grabs your wrist and leads you back to the lab where you are dismantled.\nThe bat hanging from the Laboratory ceiling shakes its head. "Maybe the next one will get away..." he says with a sigh.')
            print('You Loose, try again.')
            sys.exit() #handy command that exits the game after a loss

        if current_room == 'Backstage': #Backstage specific description and options
            print('***********************************************************************************************')
            print('While on the stage we see a realistic looking door labeled "Managers Office". We open this door to find that we are now backstage. We see a door marked exit.')
            get_items() #function call to get 'items'
            get_item() #function call to get 'item', entered here to ensure that the user is prompted to get ALL items before exiting


            leave = input('If you have the key, and wish to leave, type:Exit. Otherwise type anything else.').capitalize() #present the user with the option of leaving
            if (leave == 'Exit') and ('Master Key' in inventory) and (len(inventory) == 9):#if exit is typed and the conditions are met, then this options executes and the user wins the game
                print('***********************************************************************************************')
                print("The air is different here. It feels endless as it moves on our skin where before it smothered.")
                print("The stars overhead, the moon cresting above the skyline of the city miles off. In the moonlight")
                print("we take inventory of ourselves, of our things. We know more than we did, we know these things mean")
                print("something to us and we'll find out someday, or perhaps we won't, but we'll know we should. We'll know")
                print("at one point, we knew.")
                print('***********************************************************************************************')
                print('Thanks for playing the game, hope you enjoyed it!')
                sys.exit()
            if (leave == 'Exit') and ('Master Key' in inventory) and (len(inventory) != 9):#if exit is typed and the conditions are met, then this options executes and the user looses the game
                print('***********************************************************************************************')
                print("The air is different here. It feels endless as it moves on our skin where before it smothered.")
                print("The stars overhead, the moon cresting above the skyline of the city miles off. We hear the scuffle")
                print("of shuffling life, the shambling of feet imperfectly remembering their purpose. A mob of individuals")
                print("rise out of the dark and murmurates towards us. Its creeping swath of mismatched and malformed hands")
                print("slither over us pulling us towards the dark, towards the impossibility of the night, coil around, gouge")
                print("in, rake and tear across us as they take us away from each other. As they take us to pieces for themselves.")
                print("A bat screeches in disappointment")
                print('You Loose, try again.')
                sys.exit() #handy command that exits the game after a loss


    #if user types an invalid movement command
    else:
        print("Invalid Command! Try a different one.".format(move))
        continue

    #call function to prompt user to pick up 'item'
    get_item()
