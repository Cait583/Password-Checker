# I am importing the socket library — allowing Python to talk to other computers over a network
import socket

# Here I defined a list of common ports that can be used to check
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 8080]

# This will ask the user to type in the IP address they want to scan (example: 127.0.0.1)
target = input("Enter the target IP address: ")

# Prints a message so the user knows the scan is starting
print(f"Scanning {target}...")

# Here it will go through each port number in the common_ports list one by one
for port in common_ports:
    try:
        # Creates a socket (a network connection point)
        s = socket.socket()

        # This sets a timeout of 1 second — if the port doesn’t respond in time, it will move on to the next
        s.settimeout(1)

        # Trys to connect to the target IP on this port
        s.connect((target, port))

        # If the connection is successful, it will print that the port is open to the user
        print(f"Port {port} is OPEN")

        # Closes the socket connection
        s.close()

    except:
        # If there was an error (like port is closed), it will ignore it and move to the next port
        pass
