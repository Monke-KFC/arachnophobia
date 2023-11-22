import random
#menu function
def menu():
    menu_choice = int(input('''~~~~~~~~~~~~~~~~~~~~
1. View Context
2. Play Game
3. Leave

Please select an option: '''))
#menu choice functions start here
    def lore():
        print("\nYou are extremely afraid of spiders. You have stumbled upon a new, exquisite mantion, but it requires paperwork to be completed in order for it to stay standing. The house is littered with spiders. Can you get your work done while avoiding the spiders?!")


        
#menu choice functions end here
    if menu_choice == 1:
        lore()
        return menu()

    if menu_choice == 2:
        name = input("Please enter your player name: ")
        first_choice = input(name, "must complete some work. Will you do work, or scout out spiders? Yes, or No: ")
        if first_choice == "Yes":


        

menu()
