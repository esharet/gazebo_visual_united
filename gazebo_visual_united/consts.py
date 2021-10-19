from gazebo_unity_messages import Ack, CameraPosition, CameraConfig

class UnityConsts:
    RTSP_URL = 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'
    UNITY_COM_IP = '127.0.0.1'  
    UNITY_SOCKET_PORT = 15577 

class CameraConsts: 
    FPS = 9 
    H_FOV = 0.8726 # in radiens
    WIDTH = 640
    HEIGHT = 512 
    IS_FLIR = False
    CLIP_NEAR = 0.1
    CLIP_FAR = 500 


CAMERA_CONFIG_MSG = CameraConfig(
    width=CameraConsts.WIDTH, 
    height=CameraConsts.HEIGHT,
    h_fov=CameraConsts.H_FOV,
    fps=CameraConsts.FPS, 
    is_FLIR=CameraConsts.IS_FLIR, 
    clip_near=CameraConsts.CLIP_NEAR, 
    clip_far=CameraConsts.CLIP_FAR) 

UNITY_SOCKET_ADDRESS_PORT = (UnityConsts.UNITY_COM_IP, UnityConsts.UNITY_SOCKET_PORT)
SOCKET_TIMEOUT = 5  

BUFFER_SIZE = 1000
POSITION_UPS = 30