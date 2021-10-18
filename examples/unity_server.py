import socket
import sys
import struct

from gazebo_unity_messages import CameraConfig, CameraPosition, Ack
from gazebo_visual_united import consts 

address = ('', 15577)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server_socket.bind(address)

server_socket.settimeout(3)

def connect_client():
    connected = False
    while not connected:
        print("Listening for cam configuration")

        cam_config = CameraConfig()

        message, sender_address = server_socket.recvfrom(consts.BUFFER_SIZE)
        try: 
            cam_config.ParseFromString(message)
            ack_message = Ack()
            ack_message.ack = True
            server_socket.sendto(ack_message.SerializeToString(), sender_address)
        except Exception as e: 
            print(e)
        else: 
            print(cam_config)
            print("finished configuration ready to roll! ")
            connected = True

def recv_cam_positions():
    while True:
        print("Listening for cam position")

        cam_position = CameraPosition()

        message, sender_address = server_socket.recvfrom(consts.BUFFER_SIZE)
        try: 
            cam_position.ParseFromString(message)
        except Exception as e: 
            print(e)
        else: 
            print(cam_position)


if __name__ == "__main__": 
    connect_client()
    recv_cam_positions()