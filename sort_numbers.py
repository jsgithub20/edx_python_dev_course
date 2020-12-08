
# [ ] Write a program that reads an unspecified number of integers from the command line,
# then prints out the numbers in an ascending order
# The program should have an optional argument to save the sorted numbers as a file named `sorted_numbers.txt`

# The help message should look like:
'''
usage: sort_numbers.py [-h] [-s] [numbers [numbers ...]]

positional arguments:
  numbers     int to be sorted

optional arguments:
  -h, --help  show this help message and exit
  -s, --save  save the sorted numbers on a file (sorted_numbers.txt)
'''

#HINT: use nargs = '*' in an add_argument method

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('numbers', type = int, nargs = '*', help = 'int to be sorted')

parser.add_argument('-s', '--save', action = 'store_true', help = 'int to be sorted')

args = parser.parse_args()

print(sorted(args.numbers))

if args.save:
    with open('sorted_numbers.txt', 'w') as file:
        for num in sorted(args.numbers):
            file.write(str(num) + ' ')
    print("the sorted numbers are saved to a file 'sorted_numbers.txt'")
    
with open('sorted_numbers.txt', 'r') as file:
    print(file.readlines())