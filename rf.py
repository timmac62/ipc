#! /usr/bin/python3
import argparse

# Set up the argument parser for reading the path of the named pipe (FIFO)
parser = argparse.ArgumentParser(
    prog='rf',
    description='read and display the contents of the named fifo',
    epilog="Thanks for using %(prog)s! :)",
)

# Add an argument to specify the path of the FIFO pipe to read from
general = parser.add_argument_group("general output")
general.add_argument("fifotoread", nargs="?", default='/tmp/my_fifo')

# Parse the arguments from the command line
args = parser.parse_args()
pipe_path = args.fifotoread

# Inform the user which named pipe is being read
print(f"Reading the contents of the named pipe: {pipe_path}:")

# Continuously read from the named pipe and display its contents
while True:
    with open(pipe_path) as fifo:
        for line in fifo:
            print(line)
