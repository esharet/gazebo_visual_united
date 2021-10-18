import cv2
import os
 
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

RTSP_URL = 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'
 
 
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
 
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