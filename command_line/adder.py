
# [ ] Write a program that reads an unspecified number of integers from the command line,
# then prints out the sum of all the numbers
# the program should also have an optional argument to show the product of the numbers (in addition to the sum)


# help message should look like:
'''
usage: adder.py [-h] [-p] [numbers [numbers ...]]

positional arguments:
  numbers        numbers to be added (or multiplied)

optional arguments:
  -h, --help     show this help message and exit
  -p, --product  show the product of the numbers (in addition to the displayed
                 sum)
'''

import argparse

ap = argparse.ArgumentParser()

ap.add_argument('numbers', type = int, nargs = '*', help = 'numbers to be added (or multiplied)')
ap.add_argument('-p', '--product', action = 'store_true', help = 'show the product of the numbers (in addition to the displayed sum)')

args = ap.parse_args()

sum = 0; product = 1

for num in args.numbers:
    sum += num; product *= num

if args.product:
    print('the product is:',product)

print('the sum is:', sum)