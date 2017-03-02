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
while menu_choice != 5:
    # get menu choice from user
    menu_choice = int(input("Type in a number (1-5): "))
    
    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x,y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x,y))
            
    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = username
        
    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name: ")
        if name in usernames:
            del usernames[name]
            print("User removed")
                

    # view user name      
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        if name in usernames:
            print(usernames[name])
        else:
            print("User not found")
    
    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()