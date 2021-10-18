from threading import Thread
from gazebo_chitchat import GazeboClient
from unity_chitchat import UnityClient
import consts

def publish_poition_periodically(gazebo_client: GazeboClient, unity_client: UnityClient): 
    pass 


def main(): 
    gz_client = GazeboClient()
    unity_client = UnityClient()
    gazebo_thread = Thread(target=gz_client.start_recv_position_messages(), daemon=True)
    gazebo_thread.start()
    connection_success = unity_client.initiate_connection(consts.CAMERA_CONFIG_MSG)

    position_update_thread = Thread(target=publish_poition_periodically, daemon=True, args=(gz_client, unity_client))
    position_update_thread.start() 
    unity_client.start_rtsp_client()

if __name__ == "__main__": 
    main()