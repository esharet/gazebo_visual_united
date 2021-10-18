import cv2 
import os 

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

class UnityClient():
    def __init__(self, socket_connection_string, rtsp_url): 
        self.RTSP_URL = rtsp_url 
        self.socket_connection_string = socket_connection_string


    def initiate_connection(self,camera_config_msg): 
        pass 

    def publish_position(self, camera_position_msg): 
        pass 

    def start_rtsp_client(self,): 
        cap = cv2.VideoCapture(self.RTSP_URL, cv2.CAP_FFMPEG)
        
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
