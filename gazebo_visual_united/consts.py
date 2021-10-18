import sys 
import os
sys.path.append(sys.path[0] + '/../')
from gazebo_unity_messages import Ack, CameraPosition, CameraConfig

class UnityConsts:
    RTSP_URL = 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'
    socket_connection_string = ''   

class CameraConsts: 
    pass 

CAMERA_CONFIG_MSG = CameraConfig() 
