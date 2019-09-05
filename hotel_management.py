'''
Hotel Management App: 

    Display a menu asking whether to check in or check out.
    Prompt the user for a floor number, then a room number.
    If checking in, ask for the number of occupants and what their names are.
    If checking out, remove the occupants from that room.
    Do not allow anyone to check into a room that is already occupied.
    Do not allow checking out of a room that isn't occupied.

    Assuming hotel only has 3 floors with only rooms 101, 237, and 333.

    Wrap total script in while: True to continuously check people in and out
'''

hotel = {
    '1': {
        '101': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}


def check_in(floor, room):
    names = []
    num_guests = int(input("How many guests are with you? >> "))

    for i in range(num_guests):
        guest_name = input("Enter the guest name >> ")
        names.append(guest_name)

    hotel[floor].update({room: names})
    print(hotel)


def check_out(floor, room):
    # clear out the people in that room
    names = []

    try:
        if len(hotel[floor][room]) > 0:
            hotel[floor].update({room: names})
        else:
            print("You can't check out of a room that is empty.")
    except KeyError:
        print("You're trying to check out of a room that doesn't exist.")

    print(hotel)


while True:

    front_desk = input('Check in or check out? >>').lower()

    if front_desk == 'check in':

        floor = input('What floor would you like to stay on? >> ')
        room = input('What room number would you like? >> ')

        try:
            if len(hotel[floor][room]) > 0:
                print("That room is currently occupied at the moment")
            else:
                check_in(floor, room)

        except KeyError:
            print("That room doesn't exist in this hotel.")

    elif front_desk == 'check out':
        floor = input('What floor were you on? >> ')
        room = input('What was your room number? >> ')
        check_out(floor, room)

    else:
        print("Invalid input")
        break
