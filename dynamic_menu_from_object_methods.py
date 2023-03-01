## Python menu from object attributes and/or methods and/or properties.
# With help from: https://www.askpython.com/python/examples/find-all-methods-of-class
#                 http://openbookproject.net/pybiblio/tips/wilson/dictionaryMenus.php
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# This is our class that will have its methods listed in the menu experiment.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def say_name(self):
    print('\n################################################################################')
    print('My name is ' + self.name + '.')
    print('################################################################################')

  def say_age(self):
    print('\n################################################################################')
    print('I am ' + str(self.age) + ' years old.')
    print('################################################################################')

  def say_name_and_age(self):
    print('\n################################################################################')
    print('My name is ' + self.name + ', and I am ' + str(self.age) + ' years old.')
    print('################################################################################')


def perform_choice(chosen_method):
    eval(chosen_method) # Executes whatever the chosen method is. Executes the 'p.say_name()' string as code.
    input('Hit ENTER to continue...')


def print_menu(list):
    clear_screen()
    print(37 * "-" , "MENU" , 37 * "-")

    for count, m in enumerate(list, start = 1):
        msg = '{number}. {method}'
        msg = msg.format(number = str(count), method = m)
        print(msg)

    print("99. Exit")
    print(80 * "-")

# --------------------------------------------------------------------------------
if __name__ == '__main__':
  # Instantiating the p object as a Person.
  p = Person('Peter', 51)

  # Obtaining the list of methods available in the Person (p) object:
  # They will be:
  #     - p.say_name()
  #     - p.say_age()
  #     - p.say_name_and_age()
  methods_list = [attr for attr in dir(p) if attr.startswith('say') is True]

  # The list needs to become a dictionay so we can better access the key and the value.
  dic_list = dict(enumerate(methods_list, start = 1))

  # Creating the loop that keeps showing the menu until the user enters 99.
  loop = True
  while loop:
      print_menu(methods_list)
      choice = int(input("Enter your choice: "))
      if choice not in [99]:
          if choice in dic_list:
              # The dictionary's item value chosen (e.g.: In {2: 'say_name'...}, it is 'say_name') here is dic_list[choice]
              # The concatenation will give you 'p.say_name()' if you chose 2, for example.
              chosen_method = 'p.' + dic_list[choice] +'()'
              perform_choice(chosen_method)
          else:
              # Any integer inputs other than values 1-N or 99 we print an error message
              input("Wrong option selection. Hit ENTER to try again...")
      else:
          print("EXIT. Menu 99 has been selected.\n")
          loop = False # This will make the while loop to end as not value of loop is set to False
