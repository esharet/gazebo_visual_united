import time 
from threading import Thread
from gazebo_chitchat import GazeboClient
from unity_chitchat import UnityClient
import consts
import asyncio

def publish_poition_periodically(gazebo_client: GazeboClient, unity_client: UnityClient): 
    while True: 
        time.sleep(1/consts.POSITION_UPS)
        unity_client.publish_position(gazebo_client.camera_position)

def main(): 
    gz_client = GazeboClient()
    unity_client = UnityClient()
    loop = asyncio.get_event_loop()
    gazebo_thread = Thread(target=gz_client.start_recv_position_messages, daemon=True, args=(loop, ))
    gazebo_thread.start()
    connection_success = unity_client.initiate_connection(consts.CAMERA_CONFIG_MSG)

    position_update_thread = Thread(target=publish_poition_periodically, daemon=True, args=(gz_client, unity_client))
    position_update_thread.start() 
    unity_client.start_rtsp_client()

if __name__ == "__main__": 
    main()