from threading import Thread
from gazebo_chitchat import GazeboClient
from unity_chitchat import UnityClient
import consts


def main(): 
    gz_client = GazeboClient()
    unity_client = UnityClient(consts.connection_string, consts.rtsp_name)  
    gazebo_thread = Thread(target=gz_client.recv_messages(), daemon=True)
    gazebo_thread.start()
    connection_success = unity_client.initiate_connection(camera_config)
if __name__ == "__main__": 
    main()