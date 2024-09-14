# my_client.py

import os

# Define the path for the named pipe (FIFO)
fifo_path = "/tmp/my_fifo"

# Ensure the named pipe exists before reading from it
if not os.path.exists(fifo_path):
    print(f"Named pipe at {fifo_path} does not exist. Please run my_server.py first.")
    exit(1)

# Function to read from the named pipe
def read_from_pipe():
    with open(fifo_path, 'r') as fifo:
        print("Client: Reading from named pipe...")
        while True:
            # Read line by line from the FIFO
            message = fifo.readline().strip()
            if message:  # If a message is read
                print(f"Client: Received '{message}'")
            else:  # Break if no more messages
                break
        print("Client: Finished reading from named pipe.")

if __name__ == "__main__":
    read_from_pipe()
