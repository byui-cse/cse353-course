"""
Course: CS312
File: teach2.py
Description:
   Simple shopping list program

   You are NOT submitting this program.
"""

"""
Instructions:

Write a program that allows a user to create and use a shopping list.  Your
program will display a menu of options to the user.  The user is free
to select any option from the menu in any order.

Extra Features once you are finished with the requirements below:
1) Allow the user to enter the number of each item they want to purchase.
2) Add a "checked" feature for each item. This will be used to indicate 
   if the item is checked off the list without removing it.


Sample Output:

Welcome to the shopping list program.

Menu
   n - New shopping list item
   d - Display shopping list
   e - Edit an item in the list
   c - Check or remove item from list
   ? - Display this menu
   q - Quit program
> n
Enter shopping item: Bread
> n
Enter shopping item: Milk
> n
Enter shopping item: Eggs
> d
********* Shopping list *********
* 1  Bread                      *
* 2  Milk                       *
* 3  Eggs                       *
*********************************
> e
Which item do you want to change?: 2
Enter your change: Whole Milk
> d
********* Shopping list *********
* 1  Bread                      *
* 2  Whole Milk                 *
* 3  Eggs                       *
*********************************
> e
Which item do you want to change?: 10
Error: There is no item at that position
> e
Which item do you want to change?: 0
Error: There is no item at that position
> ?
Menu
   n - New shopping list item
   d - Display shopping list
   e - Edit an item in the list
   c - Check or remove item from list
   ? - Display this menu
   q - Quit program
> c
Which item do you want to check?: 10
Error: There is no item at that position
> c
Which item do you want to check?: 1
Item 1 was checked and removed
> d
********* Shopping list *********
* 1  Whole Milk                 *
* 2  Eggs                       *
*********************************
> n
Enter shopping item: Ice Cream
> d
********* Shopping list *********
* 1  Whole Milk                 *
* 2  Eggs                       *
* 3  Ice Cream                  *
*********************************
> q
Good bye

"""

def main():
  pass


if __name__ == "__main__":
  # execute only if run as a script
  main()
