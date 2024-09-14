#! /usr/bin/python3
# sender.py
# Usage: ./sender.py -h
import time
import argparse

# Set up the argument parser for writing to the path of the named pipe (FIFO)
parser = argparse.ArgumentParser(
    prog='sender',
    description='send message to the specified named pipe/fifo',
    epilog="Thanks for using %(prog)s! :)",
)

# Add an argument to specify the pipe path and the message
general = parser.add_argument_group("general output")
general.add_argument('fifotowrite',
            type=str,
            default='/tmp/my_fifo',
            help='The Named Pipe/FIFO to write to')
general.add_argument('opt_message_to_send',
            type=str, nargs='?',
            default='Namaste from sender',
            help='The message to send')

# Add argument to specify the number of sends
detailed = parser.add_argument_group("detailed output")
detailed.add_argument('opt_number_sends',
            type=int, nargs='?',
            default=1,
            help='An optional number of sends')

# Parse the arguments from the command line
args = parser.parse_args()
pipe_path = args.fifotowrite
message = args.opt_message_to_send
number_of_sends=args.opt_number_sends

# for debugging purposes
# print(args)
# print(f'pipe: {pipe_path}, message: {message}, number of times: {number_of_sends}')

# Inform the user which named pipe is being read
print(f"Writing to: {pipe_path}:")

# Function to send messages to the named pipe
def sender():
    # Send messages to the server
    with open(pipe_path, 'w') as fifo_write:
        for i in range(number_of_sends):
            print(f"sender: Sending '{message}'")
            fifo_write.write(message + "\n")
            fifo_write.flush()  # Ensure the message is sent immediately
            time.sleep(1)  # Simulate some delay between messages

if __name__ == "__main__":
    sender()
