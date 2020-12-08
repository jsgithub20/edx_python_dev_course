
import argparse
from random import randint

# Define an argument parser object
parser = argparse.ArgumentParser()

# Parse command-line arguments
args = parser.parse_args()

# Program
print(type(args))
print(randint(0, 10))