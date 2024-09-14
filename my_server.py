# my_server.py

import os
import time

# Define the path for the named pipe (FIFO)
fifo_path = "/tmp/my_fifo"

# Create a named pipe if it does not exist
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)
    print(f"Named pipe created at {fifo_path}")
else:
    print(f"Named pipe already exists at {fifo_path}")

# Function to write to the named pipe
def write_to_pipe():
    with open(fifo_path, 'w') as fifo:
        print("Server: Writing to named pipe...")
        for i in range(5):
            message = f"Message {i + 1} from server"
            print(f"Server: Writing '{message}'")
            fifo.write(message + "\n")
            fifo.flush()  # Ensure the message is written immediately
            time.sleep(1)  # Simulate some delay between messages
        print("Server: Finished writing to named pipe.")

if __name__ == "__main__":
    write_to_pipe()
