## Dictionary menu in Python
# This one work ok but causes an ugly message to appear after Ctrl+C is pressed,
# so I provided the two other solutions that help with that:
#    - dictionary_menu_w_catch_keyboardInterrupt_1.py
#    - dictionary_menu_w_catch_keyboardInterrupt_2.py
# Adapted from: http://openbookproject.net/pybiblio/tips/wilson/dictionaryMenus.php
import os

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

def main():
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
    clear_screen()
    main()