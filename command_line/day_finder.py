
# [ ] Write a program that reads a date (month, day, year) as command-line arguments in order
# then prints the day of the week for that date.
# If an optional flag (-c or --complete) is specified, the program should print the full date (not only the day of the week).

# The help message should look like:
'''
usage: day_finder.py [-h] [-c] month day year

positional arguments:
  month           Month as a number (1, 12)
  day             Day as a number (1, 31) depending on the month
  year            Year as a 4 digits number (2018)

optional arguments:
  -h, --help      show this help message and exit
  -c, --complete  Show complete formatted date
'''

# HINT: Use a date object with strftime

import argparse
from datetime import date

parser = argparse.ArgumentParser()

parser.add_argument('date', metavar = ('month', 'day', 'year'), nargs = 3, type = int, help = 'integer numbers represent month day year in order')

parser.add_argument('-c', '--complete', action = 'store_true', help = 'print the full date')

parser.add_argument('-v', '--verbose', action = 'store_true', help = 'Verbose mode')

args = parser.parse_args()

if args.verbose:
    print("print the full date format for {}/{}/{}:".format(month, day, year))

if args.complete:
    print(date(args[3], args[0], args[1]).strftime('%B %d, %Y, %w'))
else:
    print(date(args[3], args[0], args[1]).strftime('%w'))