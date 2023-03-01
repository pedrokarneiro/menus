## Simple text menu in Python.
# Adapted from: https://extr3metech.wordpress.com/2014/09/14/simple-text-menu-in-python/
import os, time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():       ## Your menu design here
    clear_screen()
    print(37 * "-" , "MENU" , 37 * "-")
    print("1. Menu Option 1")
    print("2. Menu Option 2")
    print("3. Menu Option 3")
    print("4. Menu Option 4")
    print("5. Exit")
    print(80 * "-")

def execute_choice(choice):
    clear_screen()
    print(choice, '\nWait 5 seconds...')
    time.sleep(5)

if __name__ == '__main__':
    loop = True
    while loop:         # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = int(input("Enter your choice [1-5]: "))
        
        if choice == 1:     
            execute_choice("Menu 1 has been selected.")
        elif choice == 2:
            execute_choice("Menu 2 has been selected.")
        elif choice == 3:
            execute_choice("Menu 3 has been selected.")
        elif choice == 4:
            execute_choice("Menu 4 has been selected.")
        elif choice == 5:
            execute_choice("Menu 5 has been selected. You are now leaving the menu program.")
            clear_screen()
            loop = False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print(an error message
            input("Wrong option selection. Hit ENTER to try again...")
