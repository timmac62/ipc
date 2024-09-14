# echo_client.py

import os
import time

# Define the path for the named pipe (FIFO)
fifo_path = "/tmp/my_fifo"

# Ensure the named pipe exists before communicating with it
if not os.path.exists(fifo_path):
    print(f"Named pipe at {fifo_path} does not exist. Please run my_server.py first.")
    exit(1)

# Function to send messages to the server and receive echoes
def client_communicate():
    print("Client: Starting communication with the server...")

    # Send messages to the server
    with open(fifo_path, 'w') as fifo_write:
        for i in range(5):
            message = f"Hello {i + 1} from client"
            print(f"Client: Sending '{message}'")
            fifo_write.write(message + "\n")
            fifo_write.flush()  # Ensure the message is sent immediately
            time.sleep(1)  # Simulate some delay between messages

    # Read the echoed messages from the server
    with open(fifo_path, 'r') as fifo_read:
        print("Client: Reading echoed messages from the server...")
        for _ in range(5):
            response = fifo_read.readline().strip()
            if response:
                print(f"Client: Received '{response}' from server")

    print("Client: Finished communication with the server.")

if __name__ == "__main__":
    client_communicate()
