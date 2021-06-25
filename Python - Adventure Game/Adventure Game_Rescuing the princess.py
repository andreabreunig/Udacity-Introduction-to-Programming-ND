import time
import random

items_events = {'sausage': 'give the sausage to the dog',
                'knife': 'fight the dog with the knife',
                'magazine': 'distract the dog with the magazine',
                'rope': 'fight the dog with the rope',
                'scissors': 'fight the dog with the scissors'}


def set_items():
    global items
    global items_kitchen
    global items_living_room
    global room
    items = []
    items_kitchen = ['knife', 'magazine', 'sausage']
    items_living_room = ['rope', 'scissors', 'sausage']
    room = random.choice(['kitchen', 'living room'])


def print_pause(message):
    print(message)
    time.sleep(2)


def introduction():
    print_pause('The princess was kidnapped.')
    print_pause('There are rumours that she was caught and trapped '
                'in the forest nearby.')
    print_pause('You have much sympathy for her. '
                'So you give it a try to find and rescue her.')
    print_pause('You drive deeply into the respective forest.')
    print_pause('After a while you reach a small intersection '
                'and get out of your car.')


def stop_playing():
    play_again = input('Would you like to play again? '
                       '(Please enter yes or no)... ').lower()
    if play_again == 'yes':
        play_game()
    elif play_again == 'no':
        print_pause('Goodbye. Have a nice day!')
    else:
        print_pause('Sorry, I don\'t understand.')
        stop_playing()


def choose_item_kitchen():
    if len(items_kitchen) == 3:
        item = input('Do you take the knife, the magazine or '
                     'the sausage?... ').lower()
    elif len(items_kitchen) == 2:
        item = input('Do you take the ' + items_kitchen[0] + ' or the ' +
                     items_kitchen[1] + '?... ').lower()
    if 'knife' in item:
        items.append('knife')
        items_kitchen.remove('knife')
        print_pause('You quickly take the knife.')
        print_pause('Then you hear some weird noise and '
                    'decide to hurry back to your car.')
        print_pause('Finally, you arrive back at your car.')
    elif 'magazine' in item:
        items.append('magazine')
        items_kitchen.remove('magazine')
        print_pause('You quickly take the magazine.')
        print_pause('Then you hear some weird noise and '
                    'decide to hurry back to your car.')
        print_pause('Finally, you arrive back at your car.')
    elif 'sausage' in item:
        items.append('sausage')
        items_kitchen.remove('sausage')
        print_pause('You quickly take the sausage with bread.')
        print_pause('Then you hear some weird noise and '
                    'decide to hurry back to your car.')
        print_pause('Finally, you arrive back at your car.')
    else:
        print_pause('Sorry, I don\'t understand.')
        choose_item_kitchen()
    choose_path()


def choose_item_living_room():
    if len(items_living_room) == 3:
        item = input('Do you take the rope, the scissors or '
                     'the sausage?... ').lower()
    elif len(items_living_room) == 2:
        item = input('Do you take the ' + items_living_room[0] + ' or the ' +
                     items_living_room[1] + '?... ').lower()
    if 'rope' in item:
        items.append('rope')
        items_living_room.remove('rope')
        print_pause('You quickly take the rope.')
        print_pause('Then you hear some weird noise and '
                    'decide to hurry back to your car.')
        print_pause('Finally, you arrive back at your car.')
    elif 'scissors' in item:
        items.append('scissors')
        items_living_room.remove('scissors')
        print_pause('You quickly take the scissors.')
        print_pause('Then you hear some weird noise and '
                    'decide to hurry back to your car.')
        print_pause('Finally, you arrive back at your car.')
    elif 'sausage' in item:
        items.append('sausage')
        items_living_room.remove('sausage')
        print_pause('You quickly take the sausage with bread.')
        print_pause('Then you hear some weird noise and '
                    'decide to hurry back to your car.')
        print_pause('Finally, you arrive back at your car.')
    else:
        print_pause('Sorry, I don\'t understand.')
        choose_item_living_room()
    choose_path()


def enter_house(room):
    print_pause('You walk towards the house and around it.')
    print_pause('On the backside, you find an open door.')
    print_pause('You enter the door and find yourself in a small kitchen.')
    if room == 'kitchen':
        if ('knife' in items_kitchen and 'magazine' in items_kitchen and
           'sausage' in items_kitchen):
            print('There is a sharp knife, a news magazine and '
                  'a delicious sausage with bread')
            print_pause('lying on the kitchen table.')
            print_pause('You can take one of these items.')
            choose_item_kitchen()
        elif 'knife' in items_kitchen and 'magazine' in items_kitchen:
            print('There is a sharp knife and a news magazine')
            print_pause('lying on the kitchen table.')
            print_pause('You can take one of these items.')
            choose_item_kitchen()
        elif 'knife' in items_kitchen and 'sausage' in items_kitchen:
            print('There is a sharp knife and a delicious sausage with bread')
            print_pause('lying on the kitchen table.')
            print_pause('You can take one of these items.')
            choose_item_kitchen()
        elif 'magazine' in items_kitchen and 'sausage' in items_kitchen:
            print('There is a news magazine and '
                  'a delicious sausage with bread')
            print_pause('lying on the kitchen table.')
            print_pause('You can take one of these items.')
            choose_item_kitchen()
        elif 'knife' in items_kitchen:
            print('You find a sharp knife')
            print_pause('lying on the kitchen table.')
            print_pause('You can take it.')
            items.append('knife')
            items_kitchen.remove('knife')
            print_pause('Then you head back to your car.')
        elif 'magazine' in items_kitchen:
            print('You find scissors')
            print_pause('lying on the kitchen table.')
            print_pause('You can take it.')
            items.append('magazine')
            items_kitchen.remove('magazine')
            print_pause('Then you head back to your car.')
        elif 'sausage' in items_kitchen:
            print('You find a delicious sausage with bread')
            print_pause('lying on the kitchen table.')
            print_pause('You can take it.')
            items.append('sausage')
            items_kitchen.remove('sausage')
            print_pause('Then you head back to your car.')
    elif room == 'living room':
        print_pause('You move forward to the living room.')
        if ('rope' in items_living_room and 'scissors' in items_living_room and
           'sausage' in items_living_room):
            print('You find a strong rope, scissors and '
                  'a delicious sausage with bread')
            print_pause('lying on the table of the living room.')
            print_pause('You can take one of these items.')
            choose_item_living_room()
        elif 'rope' in items_living_room and 'scissors' in items_living_room:
            print('You find a strong rope and scissors')
            print_pause('lying on the table of the living room.')
            print_pause('You can take one of these items.')
            choose_item_living_room()
        elif ('scissors' in items_living_room and 'sausage' in
              items_living_room):
            print('You find scissors and a delicious sausage with bread')
            print_pause('lying on the table of the living room.')
            print_pause('You can take one of these items.')
            choose_item_living_room()
        elif 'rope' in items_living_room and 'sausage' in items_living_room:
            print('You find a strong rope and a delicious sausage with bread')
            print_pause('lying on the table of the living room.')
            print_pause('You can take one of these items.')
            choose_item_living_room()
        elif 'rope' in items_living_room:
            print('You find a strong rope')
            print_pause('lying on the table of the living room.')
            print_pause('You can take it.')
            items.append('rope')
            print_pause('Then you head back to your car.')
        elif 'scissors' in items_living_room:
            print('You find scissors')
            print_pause('lying on the table of the living room.')
            print_pause('You can take it.')
            items.append('scissors')
            print_pause('Then you head back to your car.')
        elif 'sausage' in items_living_room:
            print('You find a delicious sausage with bread')
            print_pause('lying on the table of the living room.')
            print_pause('You can take it.')
            items.append('sausage')
            print_pause('Then you head back to your car.')
        else:
            print_pause('There is nothing lying in the living room.')
            print_pause('You head back to your car.')


def stay_at_lake():
    print_pause('You really enjoy your time at the beautiful lake.')
    print_pause('The time passes by quickly...')
    print_pause('... and you miss out on finding the princess.')
    print_pause('Sorry, you lost the game to find the princess.')
    stop_playing()


def choose_at_lake():
    print_pause('You can either ')
    print('1 stay at the lake and enjoy water and sunshine or')
    print('2 go to discover the house.')
    lake = input('(Please enter 1 or 2)... ')
    if lake == '1':
        stay_at_lake()
    elif lake == '2':
        enter_house(room)
    else:
        print_pause('Sorry, I don\'t understand.')
        choose_at_lake()


def left_path():
    print_pause('Ok, you walk into the direction of the lake.')
    print_pause('You arrive at a beautiful small lake with clear blue water.')
    print_pause('Next to the lake there is a small house.')
    choose_at_lake()


def choose_path():
    print_pause('Now, you need to decide to either ')
    print('1 walk into the direction of the lake or ')
    print('2 walk more deeply into the dark wood or')
    print('3 get back into your car and drive back home.')
    path = input('Where do you go? (Please enter 1, 2 or 3)... ')
    if path == '1':
        left_path()
    elif path == '2':
        right_path(items)
    elif path == '3':
        print_pause('You drive back home. It was a nice car ride. '
                    'But you didn\'t find the princess.')
        print_pause('Sorry, you lost the game.')
        stop_playing()
    else:
        print_pause('Sorry, I don\'t understand.')
        choose_path()


def dog_attack():
    print_pause('The dog attacks you. He is faster and stronger than you.')
    print_pause('You get hurt and have to quit.')
    print_pause('Unfortunately, you lost the game.')
    stop_playing()


def sausage_consequence():
    print_pause('You give the sausage to the dog.')
    print_pause('He is very happy to get something delicious to eat.')
    print_pause('While the dog is eating and starting to like you, '
                'you enter the wooden house.')
    print_pause('There is the princess smiling at you!')
    print_pause('You free her from the bonds and take her back home.')
    print_pause('You indeed succeeded to rescue the princess!!! '
                'Congratulations!!! You won the game! :-)')


def dog_event(items):
    print_pause('What do you do?')
    print('1 run back to your car')
    print('2 kick the dog with your feet')
    print('3 cuddle the dog')
    i = 1
    while i <= len(items):
        print(str(3+i) + ' ' + items_events.get(items[i-1]))
        if items[i-1] == 'sausage':
            sausage_number = i+3
        i += 1
    dog_action = input('Please enter equivalent number... ')
    if dog_action == '1':
        print_pause('You run back to your car.')
        choose_path()
    elif dog_action == '2':
        print_pause('You try to kick the dog with your feet.')
        dog_attack()
    elif dog_action == '3':
        print_pause('You try to cuddle the dog.')
        dog_attack()
    elif dog_action >= '4':
        if 'sausage' in items:
            if int(dog_action) == sausage_number:
                sausage_consequence()
            else:
                print_pause('You try to ' +
                            items_events.get(items[int(dog_action) - 4]) + '.')
                dog_attack()
        else:
            print_pause('You try to ' +
                        items_events.get(items[int(dog_action) - 4]) + '.')
            dog_attack()


def right_path(items):
    print_pause('You continue walking deeply into the woods for '
                'about half an hour.')
    print_pause('Suddenly you hear a faint voice.')
    print_pause('You recognise, this must be the princess\' voice singing.')
    print_pause('You follow the voice and reach a small wooden building.')
    print_pause('There comes a big, strong combat dog straight in front '
                'of you.')
    print_pause('He is barking at you and fletching his teeth.')
    dog_event(items)


def play_game():
    set_items()
    introduction()
    choose_path()


play_game()
