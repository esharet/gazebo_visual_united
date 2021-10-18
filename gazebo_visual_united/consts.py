from gazebo_unity_messages import Ack, CameraPosition, CameraConfig

class UnityConsts:
    RTSP_URL = 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'
    UNITY_COM_IP = '127.0.0.1'  
    UNITY_SOCKET_PORT = 15577 

class CameraConsts: 
    pass 

CAMERA_CONFIG_MSG = CameraConfig() 
UNITY_SOCKET_ADDRESS_PORT = (UnityConsts.UNITY_COM_IP, UnityConsts.UNITY_SOCKET_PORT)
SOCKET_TIMEOUT = 1

BUFFER_SIZE = 1000
POSITION_UPS = 30