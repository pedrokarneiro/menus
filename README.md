# Menus

This experiment gives us some examples of command line menus in Python.
I'm sure there are many other ways to do it and hopefully I will add them here in the future as soon as I come accross with the need.

## Menu Types Covered

The menu types covered here are meanwhile restricted to command line / shell menus, and they are:

1. simple_text_menu.py - A simple text and static menu;
2. dictionary_menu.py - A menu created from the items in a dictionary;
3. dictionary_menu_w_catch_keyboardInterrupt_1.py - The same as dictionary_menu.py, but solves the ugly KeyboardInterrupt message issue when Ctrl+C is pressed by using the "Catch the Signal" logic;
4. dictionary_menu_w_catch_keyboardInterrupt_2.py - The same as dictionary_menu.py, but solves the ugly KeyboardInterrupt message issue when Ctrl+C is pressed by using the "try-except" logic;
5. dynamic_menu_from_object_methods.py - A menu dynamically created from object attributes and/or methods and/or properties. It can be used to list any object attribute as a manu item, although one will have to adapt the logic to filter out those not wanted in the menu (edit the list comprehension - see the methods_list variable). it uses part of the logic of the dictionary_menu.py.

## Lessons Learned

Some of the examples show the end of the script by chosing a menu option, which I find simpler and more elegant.
The dictionary_menu.py example, along with the dictionary menu itself, shows the exit of the program by the Ctrl+C shortcut, which may not be very elegant, but helps us with the need to handle this kind exception. For that, we used two strategies found in dictionary_menu_w_catch_keyboardInterrupt_1.py and dictionary_menu_w_catch_keyboardInterrupt_2.py.
