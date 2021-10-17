from threading import Thread
from gazebo_chitchat import GazeboClient
from unity_chitchat import UnityClient
import consts


def main(): 
    gz_client = GazeboClient()
    unity_client = UnityClient(consts.UnityConsts.socket_connection_string, consts.UnityConsts.rtsp_connection_string)  
    gazebo_thread = Thread(target=gz_client.recv_messages(), daemon=True)
    gazebo_thread.start()
    connection_success = unity_client.initiate_connection(consts.camera_config_msg)

    unity_client.start_rtsp_client()

if __name__ == "__main__": 
    main()