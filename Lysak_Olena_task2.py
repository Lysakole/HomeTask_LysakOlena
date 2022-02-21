# I've tryed to use module argparse, but something goes wrong

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
args = parser.parse_args()
print('Hello,', args.name)



parser = argparse.ArgumentParser()
parser.add_argument('--x', type=int, required=True)
parser.add_argument('--y', type=int, required=True)
args = parser.parse_args()

model = args.x * args.y
print('Model:', model)





