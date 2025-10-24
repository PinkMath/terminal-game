# import
import os
import time
import sys

if os.name == "nt":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# Color codes
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
reset = "\033[0m"

inventory = []

def cursor_hidden():
    print("\033[?25l")

def cursor_default():
    print("\033[?25h")

def clean_terminal():
    print("\033[1;1H")
    print("\033[2J")


def inside_house(): # After entering inside the house through the window

    clean_terminal()

    print(f"{blue}Inside of the house\n\n")

    print(f"{green}Inside the old house you see a bathroom, two bedrooms, and a staircase.")

    while True:  # Keep the player inside the house until they make a valid choice
        print(f"\n{cyan}What will you do?")
        print(f"{cyan}1. Go up the stairs")
        print(f"{cyan}2. Check the bathroom")
        print(f"{cyan}3. Check both bedrooms")
        print(f"{cyan}4. Inventory")
        print(f"{cyan}5. come back")

        choice = input(f"{cyan}Enter your choice (1-3): ")

        if choice == '1':
            print(f"\n{white}While you were going up the stairs, you heard footsteps. Maybe it's not a good idea to go up there...")
        elif choice == '2':

            if "gas mask" in inventory:
                bathroom_hide()
            else:
                print(f"\n{white}You went into the bathroom, but it's horrible inside. You can't go there now...")
        elif choice == '3':
            first_room()
            second_room()
        elif choice == '4':
            show_inventory()
        elif choice == '5':
            game()
        else:
            print(f"{red}Invalid choice, please select between 1 and 4.")

def first_room(): # when u go cheack the bedrooms first ill always 'auto' cheack the first room and then the second

    clean_terminal()

    print(f"{blue}Inside of the house - first bedroom\n\n")

    print(f"{white}You went inside the first bedroom and didn't see anything useful, only a key on the bed.")

    take_key = "" # dont add anything here to make whats in the under line
    while take_key not in ['y', 'n', 'yes', 'no']: # if the anwer aint these options it wont work
        take_key = input(f"\n{cyan}Take the key? (y/n or yes/no): ").lower() # to make a loop till the anwer be right
    
    if take_key == 'y' or take_key == 'yes':
        print(f"\n{red}It was a trap! A hand under the bed grabs your leg and pulls you under. All that remains of you is a pool of blood.")
        print(f"\n{red}GAME OVER")
        print("\033[?25h")
        sys.exit() # End the game here
    elif take_key == 'n' or take_key == 'no':
        print(f"\n{white}It looks too weird, why would a key be on the bed? You decide to change rooms.")
        time.sleep(3)
        return
    else:
        print(f"{red}Please enter 'y/n' or 'yes/no'.")  # If the input is invalid, keep looping

def second_room(): # when u cheack the bedrooms after u cheack the first 

    clean_terminal()

    print(f"{blue}Inside of the house - second bedroom\n\n")

    while True:
        print(f"{green}In the second room's a nightstand and a cupboard.\n")

        print(f"{cyan}What you wanna cheack first?")
        print(f"{cyan}1. nightstard")
        print(f"{cyan}2. copboard")
        print(f"{cyan}3. come back")
        print(f"{cyan}4. inventory")

        choice = input(f"{cyan}Enter your choice (1-4): ")

        if choice == '1':
            print(f"\n{white}You decides to cheack the nightstand first, opening the drawers you found a gas mask")

            if "gas mask" in inventory:
                print(f"\n{red}You already have one gas mask.")
            else:
                gasmask_choice = ""
                while gasmask_choice not in ['y', 'n', 'yes', 'no']:
                    gasmask_choice = input(f"\n{green}Do you want to take it (y/n or yes/no)? ").lower()
                
                if gasmask_choice == 'y' or gasmask_choice == 'yes':
                    print(f"\n{white}You took the mask.")
                    inventory.append("gas mask") # add gas mask in the inventory
                elif gasmask_choice == 'n' or gasmask_choice == 'no':
                    print(f"\n{white}You didn't take the mask.")
                else:
                    print(f"\n{red}Please enter 'y/n' or 'yes/no'.")  # If the input is invalid, keep looping

                
        elif choice == '2':
            print(f"\n{white}That's anything in there only old papers.")
        elif choice == '3':
            inside_house()
        elif choice == '4':
            show_inventory()
        else:
            print(f"{red}Invalid choice, please select between 1 and 4.")
            

def bathroom_hide(): # when ur in the bathroom and u gotta hide to dont die

    clean_terminal()
    

    print(f"{blue}Bathroom\n\n")

    if "shovel" in inventory:
        print(f"{white}You were here before, it's not safe.")
        time.sleep(3)
        inside_house()
    else:
        print(f"\n{white}Even with the gas mask the place smells horrible. You look around but you can't see much")
        print(f"{white}but you can to see there's something in the sink, when you were about to see you heard someone")
        print(f"{white}comming to the bathroom. You gotta hide!")

        while True:
            print(f"\n{magenta}Where do you wanna hide?")
            print(f"{magenta}1. behind the sink")
            print(f"{magenta}2. behind the door")
            print(f"{magenta}3. behind the body")

            choice = input(f"{magenta}Enter your choice (1-3): ")

            if choice == '1':
                print(f"\n{red}You tried to hide behind the sink, but even with the place dark he could see you. He killed you.")
                print(f"\n{red}GAME OVER")
                sys.exit() # to exit of the game
            elif choice == '2':
                print(f"\n{red}You tried to hide behind the door, he didn't see you at first but when he was about to live he saw something behind the door. He broke your neck")
                print(f"\n{red}GAME OVER")
                sys.exit() # to exit of the game
            elif choice == '3':
                print(f"\n{white}You tried to hide behind the body in the corner, you found out where the smell's comming from.")
                print(f"{white}After all he didn't see you thinking it was just another body")

                print(f"\n{green}Now that he's gone you realise there's a shovel inside of the body")


                shovel_input = ""
                while shovel_input not in ['y', 'yes', 'n', 'no']:
                    shovel_input = input(f"\n{cyan}Wanna take it? (y/n or yes/no): ").lower()
                    
                    if shovel_input == 'y' or shovel_input == 'yes':
                        inventory.append("shovel")
                        inside_house()
                    elif shovel_input == 'n' or shovel_input == 'no':
                        inside_house() 
                    else:
                        print(f"{red}Only 'y/n' or 'yes/no'")
            else:
                print(f"\n{red}Invalid choice, please select between 1 and 3.")


def back_house(): # u can to go behind the house to make other ends
    
    clean_terminal()

    print(f"{blue}Behind of the house\n\n")

    print(f"{green}That's nothing much in here, only a old stable and a cave.")

    while True:
        print(f"\n{cyan}Do you wanna cheack something?")
        print(f"{cyan}1. Cave")
        print(f"{cyan}2. Stable")
        print(f"{cyan}3. Inventory")
        print(f"{cyan}4. Come back")

        choice = input(f"{cyan}Enter your choice (1-4): ")

        if choice == '1':
            if "shovel" in inventory:
                inside_stable() # inside of the stable after digging the hole outside
            else:
                print(f"{white}You walked around the cave looking for a hole to you pass through, but seems like you gonna need a shovel")
        elif choice == '2':
            print(f"\n{white}It's locked, looks like you gotta find a key")
        elif choice == '3':
            show_inventory()
        elif choice == '4':
            game()
        else:
            print(f"\n{red}Invalid choice, please select between 1 and 4.")

def inside_stable(): # inside of the stable
    clean_terminal() # itll restart the terminal

    print(f"{blue}Inside of the stable\n")

    print(f"\n{white}You finally can to see where this cave gonna let you. While you were digging the hole you got inside of the stable.")
    print(f"\n{green}You can to see there's only old weapons inside that looks really old, but thats some knifes on the talbe.")

    while True:
        print(f"\n{cyan}1. table")
        print(f"{cyan}2. weapons")
        print(f"{cyan}3. inventroy")
        print(f"{cyan}4. come back")
        
        choice = input(f"{cyan}What do you wanna do (1-4):")

        if choice == '1':
            if "knife" in inventory:
                print(f"\n{white}You went back to the table but you all of the knifes're old, you already took the best one")
            else:
                print(f"\n{green}You walked in front of the table and there's alot of different knifes")


                knife_choice = ""
                while knife_choice not in ['y', 'yes', 'n', 'no']:
                    knife_choice = input(f"\n{cyan}Would you like to take a knife? ('y/n' or 'yes/no'): ").lower()
                    
                    if knife_choice == 'y' or knife_choice == 'yes':
                        print(f"\n{white}You took the knife that looks ok, because all of the others looks like it's about to break")
                        inventory.append("knife")
                    elif knife_choice == 'n' or knife_choice == 'no':
                        print(f"\n{white}You deside to dont take the knife")
                    else:
                        print(f"\n{red}Only 'y/n' or 'yes/no'")

        elif choice == '2':
           print(f"\n{white}You went to cheack if there's at least one weapon working and any of them are...")
        elif choice == '3':
            show_inventory()
        elif choice == '4':
            back_house()
        else:
            print(f"{red}Invalid choice, please select between 1 and 4.")
                    

def game():
    cursor_hidden()
    clean_terminal()
    print(f"{blue}Outside of the house\n\n")
    print(f"{green}You and your friend decide to go into a weird old house.")
    print(f"{green}Your friend went in first, but you were too scared to go with him.")
    print(f"{green}A few minutes later, there's still no sign of your friend...")
    print(f"{green}Should you enter the house to look for him?\n")

    while True:

        print(f"\n{cyan}What will you do?")
        print(f"{cyan}1. Enter the house to look for your friend")
        print(f"{cyan}2. Call for help and wait outside")
        print(f"{cyan}3. Leave the house and go back home")
        print(f"{cyan}4. Try to find another way in (through a window, etc.)")
        print(f"{cyan}5. Inventory")
        print(f"{cyan}6. Behind the house")
        print(f"{cyan}7. Quit the game")

        choice = input(f"{cyan}Enter your choice (1-7): ")

        if choice == '1':
            print(f"\n{white}The front door's stuck. You can't get inside that way.")
        elif choice == '2':
            print(f"\n{white}You shout for help, but there’s no response. The silence is eerie. You start to feel uneasy about your decision.")
        elif choice == '3':
            print(f"\n{white}You decide it's too dangerous and leave, heading back home. But deep down, you feel guilty for not helping your friend.")
            print(f"\n{blue}End game(1/&)")
            print("\033[?25h")
            sys.exit()  # Exit the game or scenario
        elif choice == '4':
            print(f"\n{white}You look around the house for another way in. You spot an old, cracked window. You decide to climb through it.")
            time.sleep(3)
            inside_house()  # Call the function to handle the new inside scenario
        elif choice == '5':
            show_inventory()
        elif choice == '6':
            back_house()
        elif choice == '7':
            print(f"\n{red}You quit the game. Goodbye!")
            print("\033[?25h")
            sys.exit()  # End the game
        else:
            print(f"{red}Invalid choice, please select between 1 and 7.")

def show_inventory():
    # show the inventory
    if inventory:
        print(f"\n{yellow}Inventory:")
        for item in inventory:
            print(f"- {item}")
    else:
        print(f"\n{red}Your inventory's empty")

# start the game
game()

