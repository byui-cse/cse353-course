"""
Course: CS312
File: project02.py
Description:
   Numpy and MatPlotlib project

   You are submitting this project to Canvas when completed
"""

"""
Instructions:

0) You must only use numpy and matplotlib for this project.
   No other packages.  You can use Python lists/dictionaries.

1) Download the CSV files from GitHub for this project

2) You will be creating functions to load these CSV files in a numpy array
   (One at a time)

3) For each CSV file, you will be creating multiple plots.
   You can decide on the type of plot(s) to create.
   Make sure that you are able to display the information clearly.
   I would add labels and anything that makes the plots look good.
   Use the show() function in MatPlotLib to display each plot.

  a) Plot all of the temperatures found in the CSV
  b) Plot only the August temperatures
  c) Average each years' worth of temperatures and plot these values
     (year vs average temp)

4) You should be creating 6 plots.

5) Create functions and add comment to them.

Data Files:
- newzealand.csv
- paris.csv

Sample data in the paris.csv file

month,year,temp
10,1752,50.4338
11,1752,45.473
12,1752,40.928
1,1753,31.9046
2,1753,38.7698
3,1753,46.3352
4,1753,48.7526
5,1753,56.5736
6,1753,65.3234
7,1753,66.4754
8,1753,62.6
9,1753,59.7434
"""

import matplotlib.pyplot as plt
import numpy as np


def process_file(filename):
    """ Create the three plots """
    pass


def main():
    """ Main function """

    for filename in ['newzealand.csv', 'paris.csv']:
        process_file(filename)


if __name__ == "__main__":
    # execute only if run as a script
    main()
