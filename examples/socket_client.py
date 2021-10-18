import socket
import sys
import struct
import time
from gazebo_unity_messages import CameraPosition

address = ('localhost', 6005)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
connected = False
while not connected: 

    print(f"is connected 1 : {connected}")
    try: 
        client_socket.connect(address)
        client_socket.sendall(b'sdfjl')
        client_socket.sendall(b'sdfjl')
        connected = True
    except Exception as e: 
        print(f" connection failed due to:{str(e)}, retrying...")
        time.sleep(1)
    print(f"is connected 2 : {connected}")
messages = ["foobar", "barbaz", "bazquxfad", "Jimmy Carter"]

print("got hereeeeee")
cam_pose = CameraPosition()
cam_pose.latitude = 7 

for i in range(10):
    time.sleep(1/30)
    client_socket.sendall(cam_pose.SerializeToString())
    print(f"sent {cam_pose.SerializeToString()}")