from gazebo_unity_messages import CameraConfig, CameraPosition

from pygazebo import pygazebo
from pygazebo import msg
import asyncio
from transformations import euler_from_quaternion
from dataclasses import dataclass, field

@dataclass
class orientation():
    x: float = None
    y: float = None
    z: float = None
    w: float = None

@dataclass
class vector():
    x: float = None
    y: float = None
    z: float = None

@dataclass
class IMU():
    entity_name: str
    orientation: orientation
    angular_velocity: vector
    linear_acceleration: vector

@dataclass
class GPS():
    link_name: str = None
    latitude_deg: float = None
    longitude_deg: float = None
    altitude: float = None
    velocity_east: float = None
    velocity_north: float = None
    velocity_up: float = None

@dataclass
class GazeboData():
    imu: IMU
    gps: GPS


GZ_IMU_TOPIC = "/gazebo/default/iris_demo/iris_demo/iris/iris/imu_link/imu_sensor/imu"
GZ_GPS_TOPIC = "/gazebo/default/iris_demo/iris_demo/iris/base_link/gps_sensor/gps"


class GazeboClient(): 
    def __init__(self,): 
        self.camera_position = CameraPosition()
        self.camera_position.latitude = 4
        self.gazebo_data = GazeboData(imu=None, gps=None)

    def handler_imu(self, data):
        imu_msg = msg.imu_pb2.IMU()
        imu_msg.ParseFromString(data)
        self.gazebo_data.imu = imu_msg
        imu_euler = euler_from_quaternion([self.gazebo_data.imu.orientation.x,self.gazebo_data.imu.orientation.y,self.gazebo_data.imu.orientation.z,self.gazebo_data.imu.orientation.w])
        self.camera_position.roll = imu_euler[0]
        self.camera_position.pitch = imu_euler[1]
        self.camera_position.yaw = imu_euler[2]

    def handler_gps(self, data):
        gps_msg = msg.gps_pb2.GPS()
        gps_msg.ParseFromString(data)
        self.gazebo_data.gps = gps_msg
        self.camera_position.latitude = self.gazebo_data.gps.latitude_deg
        self.camera_position.longitude = self.gazebo_data.gps.longitude_deg
        self.camera_position.altitude = self.gazebo_data.gps.altitude
        self.camera_position.vel_east = self.gazebo_data.gps.velocity_east
        self.camera_position.vel_north = self.gazebo_data.gps.velocity_north
        self.camera_position.vel_up = self.gazebo_data.gps.velocity_up


        # print(self.camera_position)

    async def subscribe_position(self,):
        manager = await pygazebo.connect()
        await manager.subscribe(GZ_IMU_TOPIC, 'gazebo.msgs.IMU', self.handler_imu)
        await manager.subscribe(GZ_GPS_TOPIC, 'gazebo.msgs.GPS', self.handler_gps)
        

        while True:
            await asyncio.sleep(1)

    def start_recv_position_messages(self,loop): 
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.subscribe_position())


if __name__ == "__main__": 
    gazebo_client = GazeboClient()
    loop = asyncio.get_event_loop()
    gazebo_client.start_recv_position_messages(loop)