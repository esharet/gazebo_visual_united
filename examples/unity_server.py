import socket
import sys
import struct

from gazebo_unity_messages import CameraConfig, CameraPosition, Ack
from gazebo_visual_united import consts 

address = ('', 15577)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server_socket.bind(address)

server_socket.settimeout(3)

while True:
    print("Listening")

    # totallen = server_socket.recv(4)
    # totallenRecv = struct.unpack('>I', totallen)[0]
    # messagelen = totallenRecv - 4
    cam_config = CameraConfig()

    message, sender_address = server_socket.recvfrom(1000)
    print(sender_address)
    print('after message')
    try: 
        cam_config.ParseFromString(message)
        ack_message = Ack()
        ack_message.ack = True
        server_socket.sendto(ack_message.SerializeToString(), sender_address)
    except Exception as e: 
        print(e)
    else: 
        print(cam_config)