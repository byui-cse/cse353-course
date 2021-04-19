"""
Course: CSE 353
Lesson Week: 01
File: teach2.py
Author: Brother Comeau
Problems taken from: https://edabit.com/challenges/python3
"""

""" 
A number is said to be Disarium if the sum of its digits raised to their 
respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.

Examples
disarium(75) ➞ False   # 7^1 + 5^2 = 7 + 25 = 32
disarium(135) ➞ True   # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
disarium(544) ➞ False
disarium(518) ➞ True
disarium(466) ➞ False
disarium(8) ➞ True
"""
def disarium(value):
    pass


"""
Valid Hex Code
Create a function that determines whether a string is a valid hex code.

A hex code must begin with a pound key # and is exactly 6 characters 
in length. Each character must be a digit from 0-9 or an alphabetic 
character from A-F. All alphabetic characters may be uppercase or lowercase.

Examples
is_valid_hex_code("#CD5C5C") ➞ True
is_valid_hex_code("#EAECEE") ➞ True
is_valid_hex_code("#eaecee") ➞ True
is_valid_hex_code("#CD5C58C") ➞ False   # Length exceeds 6
is_valid_hex_code("#CD5C5Z") ➞ False    # Not all alphabetic characters in A-F
is_valid_hex_code("#CD5C&C") ➞ False    # Contains unacceptable character
is_valid_hex_code("CD5C5C") ➞ False     # Missing #
"""
def is_valid_hex_code(code):
    pass


"""
Valid matching ()

Create a function to takes a given string and returns True if the () match

matching_brackets('()')  -> True
matching_brackets('(3 + 8)')  -> True
matching_brackets('(()())')  -> True
matching_brackets('(cat((house)()))')  -> True
matching_brackets('((())))(')  -> False
matching_brackets('())')  -> False
"""

def matching_brackets(expression):
    pass

"""
LCM of More Than Three Numbers
Create a function that takes a list of more than three numbers and returns
the Least Common Multiple (LCM).  The LCM of a list of numbers is the 
smallest positive number that is divisible by each of the numbers in the list.

Examples
get_lcm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 2520
get_lcm([13, 6, 17, 18, 19, 20, 37]) ➞ 27965340
get_lcm([44, 64, 12, 17, 65]) ➞ 2333760
"""
def get_lcm(values):
    pass


"""
Letter Shifting
Create a function that takes a string and shifts the letters to the right by an amount n but not the whitespace.

Examples
shift("Boom", 2) ➞ "omBo"

shift("This is a test",  4) ➞ "test Th i sisa"

shift("A B C D E F G H", 5) ➞  "D E F G H A B C"
Notes
Keep the case as it is.
n can be larger than the total number of letters.
"""
def shift(sentence, amount):
    pass



def main():

    # TODO - comment out the function that you are testing

    # assert(disarium(544) == False)
    # assert(disarium(518) == True)
    # assert(disarium(466) == False)
    # assert(disarium(8) == True)


    # assert(is_valid_hex_code("#CD5C5C") == True)
    # assert(is_valid_hex_code("#EAECEE") == True)
    # assert(is_valid_hex_code("#eaecee") == True)
    # assert(is_valid_hex_code("#CD5C58C") == False)
    # assert(is_valid_hex_code("#CD5C5Z") == False)
    # assert(is_valid_hex_code("#CD5C&C") == False)
    # assert(is_valid_hex_code("CD5C5C") == False)


    # assert(matching_brackets('()') == True)
    # assert(matching_brackets('(3 + 8)') == True)
    # assert(matching_brackets('(()())') == True)
    # assert(matching_brackets('(cat((house)()))') == True)
    # assert(matching_brackets('((())))(') == False)
    # assert(matching_brackets(')(') == False)


    # assert(get_lcm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2520)
    # assert(get_lcm([13, 6, 17, 18, 19, 20, 37]) == 27965340)
    # assert(get_lcm([44, 64, 12, 17, 65]) == 2333760)


    # assert(shift("Boom", 2) == 'omBo')
    # assert(shift("A B C D E F G H", 5) == 'D E F G H A B C')

    pass


if __name__ == '__main__':
    main()
