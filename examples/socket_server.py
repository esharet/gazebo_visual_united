import socket
import sys
import struct

from gazebo_unity_messages import CameraPosition

address = ('', 15577)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server_socket.bind(address)


while True:
    print("Listening")

    # totallen = server_socket.recv(4)
    # totallenRecv = struct.unpack('>I', totallen)[0]
    # messagelen = totallenRecv - 4
    cam_pose = CameraPosition()
    message = server_socket.recv(1000)
    print('after message')
    try: 
        cam_pose.ParseFromString(message)
    except Exception as e: 
        print(str(e))
    else: 
        print(cam_pose)