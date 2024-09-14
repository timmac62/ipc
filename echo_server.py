# echo_server.py

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
def echo_server():
    print("Server: Waiting for messages from the client...")

    # Open the pipe for reading messages from the client
    with open(fifo_path, 'r') as fifo_read:
        while True:
            # Read line by line from the FIFO
            message = fifo_read.readline().strip()
            if message:  # If a message is read
                print(f"Server: Received '{message}' from client")

                # Echo back the message to the client
                response = f"Echo: {message}"
                print(f"Server: Sending back '{response}'")

                # Open the pipe in write mode to send the response
                with open(fifo_path, 'w') as fifo_write:
                    fifo_write.write(response + "\n")
                    fifo_write.flush()
            else:
                break

    print("Server: Finished echoing messages.")

if __name__ == "__main__":
    echo_server()
