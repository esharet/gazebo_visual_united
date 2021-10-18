import socket 
import time

import cv2 
import os

from gazebo_unity_messages import CameraPosition
from gazebo_unity_messages.py_msgs.ack_pb2 import Ack 
from gazebo_visual_united import consts

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

def prepare_msg(serialized_msg: bytes): 
    return serialized_msg

class UnityClient():
    def __init__(self, ): 
        self.unity_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.unity_socket.settimeout(consts.SOCKET_TIMEOUT)
        
    def initiate_connection(self,camera_config_msg): 
        connected = False
        while not connected: 
            try: 
                self.unity_socket.connect(consts.UNITY_SOCKET_ADDRESS_PORT)
                msg_to_send = prepare_msg(camera_config_msg.SerializeToString())
                self.unity_socket.sendall(msg_to_send)
                self.unity_socket.sendall(msg_to_send)
            except Exception as e: 
                print(f"error in connection, trying again... ")
                time.sleep(1)
            else:
                try: 
                    message = self.unity_socket.recv(consts.BUFFER_SIZE) 
                    response = Ack()
                    response.ParseFromString(message)
                    if response.ack: 
                        print("connection successfull!!")
                        connected = True
                except Exception as e:
                    print(f"error in response from server, trying again... ")
                    time.sleep(1)

        return True

    def publish_position(self, camera_position_msg: CameraPosition): 
        msg_to_sent = prepare_msg(camera_position_msg.SerializeToString())
        self.unity_socket.sendall(msg_to_sent)

    def start_rtsp_client(self,): 
        cap = cv2.VideoCapture(consts.UnityConsts.RTSP_URL, cv2.CAP_FFMPEG)
        
        if not cap.isOpened():
            print('Cannot open RTSP stream')
            exit(-1)
        
        while True:
            _, frame = cap.read()
            cv2.imshow('RTSP stream', frame)
        
            if cv2.waitKey(1) == 27:
                break
        
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__': 
    unity_client = UnityClient() 
