
# [ ] The following program generates a staircase character art
# The `size` variable controls the number of steps
# The `base_shape` defines the characters used to generate the art
# Modify the program so the `size` is set as a positional command line argument, and base_shape as an optional 
# command line argument with a default value of `[]`

import argparse

ap = argparse.ArgumentParser()

ap.add_argument('steps', metavar = 'size', type = int, help = 'Number of steps')
ap.add_argument('-b', '--base_shape', metavar = 'base_shape', nargs = 1, default = ['[]'], help = 'the characters used to generate the art')

args = ap.parse_args()        

def gen_stairs(steps, base_shape):
    for row in range(steps):
        for col in range(steps):
            if(col <= row):
                print(base_shape, end = "")
        print()

# Generate a staircase with 6 steps using '[]` as a base shape               

gen_stairs(args.steps, args.base_shape[0])