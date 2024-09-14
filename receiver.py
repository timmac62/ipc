#! /usr/bin/python3
# receiver.py
# the receiver
import os

# Define the path for the named pipe (FIFO)
fifo_path = "/tmp/my_fifo"

# Create a named pipe if it does not exist
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)
    print(f"Named pipe created at {fifo_path}")
else:
    print(f"Named pipe already exists at {fifo_path}")

# Function to read from and write to the named pipe
def receiver():
    print("receiver: Waiting for messages from the sender...")

    # Open the pipe for reading messages from the sender
    with open(fifo_path, 'r') as fifo_read:
        while True:
            # Read line by line from the FIFO
            message = fifo_read.readline().strip()
            if message:  # If a message is read
                print(f"receiver: Received '{message}' from sender")
            else:
                break

    print("receiver: Finished echoing messages.")

if __name__ == "__main__":
    receiver()
