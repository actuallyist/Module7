# Assignment 7
# by Sarah Rambeau

"""This script allows the user to look through a list of current users,
and add and delete entries.  I have added exception handling to throw errors
when the user does not pick a valid menu option.  I have also added assert
statements to inform the user if their input is not found or is not allowed
"""

#!/usr/bin/env python

from sortedcontainers import SortedDict

def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print()

# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

#display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
# if the user enters a non-integer, they are told this is not a valid option
while menu_choice != 5:
    # get menu choice from user
    try:
        menu_choice = int(input("Type in a number (1-5): "))
    except ValueError:
        print("That is not a valid option.")
    
    # view current entries
    # if there are no entries in the dictionary, a message is shown
    if menu_choice == 1:
        print("Current Users:")   
        try:
            assert len(usernames) != 0
            for x,y in usernames.items():
                print("Name: {} \tUser Name: {} \n".format(x,y))
        except AssertionError:
            print("There are no current users.")


    # add an entry
    # the user may not add a blank entry
    # the user's name must contain at least one letter
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        try:
            assert len(name) !=0
            assert len(username) != 0
            assert name.isdigit() == False
            usernames[name] = username
        except AssertionError:
            print("Invalid Entry.  Name must contain at least one letter.")
        
    # remove an entry
    # if the name is not in the dictionary, the user is told
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name: ")
        try:
            assert usernames[name] != 0
            if name in usernames:
                del usernames[name]
                print("User removed.")
        except KeyError:
            print("Name not found.")
                

    # view user name
    # as above, name must contain at least one letter
    # if only numbers are entered, an error is shown      
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        try:
            assert name.isdigit() == False
            if name in usernames:
                print(usernames[name])
            else:
                print("User not found.")
        except AssertionError:
            print("Why would you enter all numbers?  That is not a name.")
    
    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()