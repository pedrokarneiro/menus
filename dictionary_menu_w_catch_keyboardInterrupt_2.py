## Dictionary menu in Python
# Catching the ugly KeyboardInterrupt message when Ctrl+C is pressed.
# Strategy #2: Using "try-except" logic.
# Adapted from: http://openbookproject.net/pybiblio/tips/wilson/dictionaryMenus.php
#               https://zeldor.biz/2019/12/catch-keyboardinterrupt/
import os, sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def printForward(word):
    print('\nWord: ')
    for chr in word:
        print(chr, end='')
    print('\n')

def printBackward(word):
    print('\nWord in backards: ')
    for i in range(len(word)-1, -1, -1): # count backward from the end of word
        print(word[i], end='')
    print('\n')

def menu():
    menu = {'F': printForward,
            'B': printBackward}
    while 1:
        try:
            word = input("Type a word (or Ctrl-C to quit): ")
        except EOFError:
            print("Bye.")
            break
        prompt = "'%s'\n(F)orward or (B)ackward? " % word
        choice = (input(prompt)).upper()
        try:
            menu[choice](word)
        except KeyError:
            print("'%s' is not a valid option. Try again." % choice)

if __name__ == '__main__':
    try:
        while True:
            clear_screen()
            menu()
    except KeyboardInterrupt:
        # KeyboardInterrupt has been catched!
        clear_screen()
        sys.exit(0)
