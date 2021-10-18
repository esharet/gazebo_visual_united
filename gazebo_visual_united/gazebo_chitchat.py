from gazebo_unity_messages import CameraConfig, CameraPosition

class GazeboClient(): 
    def __init__(self,): 
        self.camera_position = CameraPosition()
        self.camera_position.latitude = 4

    def start_recv_position_messages(self,): 
        pass