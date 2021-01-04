"""
Course: CS312
File: teach1.py
Description:
   Simple Numpy problems

   You are NOT submitting this program.
"""

"""
Instructions:

- You will creating numpy arrays in the following functions

"""
import numpy as np

def task1():
    """ create an array of size 10 of zeros """

    # Replace 'None' with the array you create
    return None


def task2():
    """ Create array of ones of size 20 """

    # Replace 'None' with the array you create
    return None


def task3():
    """ Create array of ones that are integers of size 10 """

    # Replace 'None' with the array you create
    return None


def task4():
    """ create 4 dim array of size (10, 3, 4, 5) of integers.
        Make sure that no integer repeats in the array
    """

    # Replace 'None' with the array you create
    return None


def task5():
    """ Create array of 100 random values and create another one where
    values equal and over 0.5 are set to 1.0 and values less than
    0.5 are set to 0.0
    """

    # Replace 'None' with the array you create
    return None


# Word Search
def word_search():
    """ 
    the file wordsearch.txt contains a word search puzzle.

    1) Download the wordsearch.txt file from GitHub
    2) Load the puzzle into a numpy array
    3) write code/functions to find the following words in the puzzle
    4) Some of the words below are not in the puzzle
    
    Hint: I would place the words below in a Python list
    Hint: I would create a function that takes the puzzle and one word
          and returns True / False if it is found

    Word List
    =========
    BYUI
    COMPUTER
    CPYTHON
    GRAPHICS
    HOUSE
    IDAHO
    KEYBOARD
    LINUX
    MATPLOTLIB
    NUMPY
    PACKAGES
    PYTHON
    TREE
    VISION
    WINTER
    """

    # TODO Indicate which words at found in the puzzle and which ones are not
    pass



def main():
    """ Main function """

    a = task1()
    print(f'Task 1:\n{a}\n')

    a = task2()
    print(f'Task 2:\n{a}\n')
    
    a = task3()
    print(f'Task 3:\n{a}\n')
    
    a = task4()
    print(f'Task 4:\n{a}\n')

    a = task5()
    print(f'Task 5:\n{a}\n')

    word_search()



if __name__ == "__main__":
    # execute only if run as a script
    main()
