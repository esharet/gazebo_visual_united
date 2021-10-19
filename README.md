# gazebo_visual_united
## system requirements
1. Ubuntu 20 
2. python3 installed 

## installation 
1. clone the project into ~/projects directory 
2. [gazebo installation](http://gazebosim.org/tutorials?tut=install_ubuntu)
   1. after installation run ```source /usr/share/gazebo-11/setup.py```
   2. 
   ```
   sudo apt-get update 
   sudo apt-get install -y build-essential
   ```
   3. run the following lines (to add mendatory lines to ~/.bashrc):
       ```
       echo 'source /usr/share/gazebo-11/setup.sh' >> ~/.bashrc
       echo 'export GAZEBO_MODEL_PATH=~/projects/gazebo_visual_united/models:${GAZEBO_MODEL_PATH}' >> ~/.bashrc
       echo 'export GAZEBO_RESOURCE_PATH=~/projects/gazebo_visual_united/worlds:${GAZEBO_RESOURCE_PATH}' >> ~/.bashrc
       echo 'export GAZEBO_PLUGIN_PATH=~/apm/gazebo_visual_united/build:${GAZEBO_PLUGIN_PATH}' >> ~/.bashrc
       source ~/.bashrc
       ```

    4. compile the plugins:
       ```
       cd build
       cmake ..
       make
       sudo make install
       ```
   3. test gazebo with the world - ```gazebo /home/user/projects/gazebo_visual_united/worlds/iris_arducopter_runway.world --verbose```

3. [sitl installation](https://ardupilot.org/dev/docs/building-setup-linux.html#building-setup-linux)
   1. follow the installation process and clone the ardupilot project to ~/apm directory (or update all paths accordingly) 
   2. test sitl 
   ``` sim_vehicle.py -v ArduCopter --map```
   1. the first run should build a lot of packages so this might take a while 
   2. sitl-gazebo test
   in terminal 1 - 
   ```gazebo /home/user/projects/gazebo_visual_united/worlds/iris_arducopter_runway.world --verbose```
   in terminal 2 - 
   ```sim_vehicle.py -v ArduCopter -f gazebo-iris --map``` 

   1. controlling the vehicle should work and be seen in the gazebo.
   in terminal 2 - 
   ```
   param set DISARM_DELAY 0
   arm throttle 
   mode GUIDED 
   takeoff 50
   ```
4. Optional - installing dronekit for [basic mission](https://dronekit-python.readthedocs.io/en/latest/examples/mission_basic.html) script: 
   1. ```pip install dronekit dronekit-sitl```  
   2. clone http://github.com/dronekit/dronekit-python.git (in ~/projects directory)
   3. cd ~/projects/dronekit-python/examples/vehicle_state/
   4. instead of step 5 last section. running ```python mission_basic.py --connect 127.0.0.1:14550```
   needs to do a mission in and be seen in the gazebo and sitl map.

5. install the project  
   1. 
   2. ```python3 -m venv venv```
   3. in the venv - 
      1. ``` python3 -m pip --upgrade pip setuptools wheel```
      2. ```pip install -r requirements```
   4. generating the messages - 
      1. in the gazebo_unity_messages dir - ```protoc -I=proto --python_out=py_msgs proto/*```
   5. setup - 
      1. in the project root dir - ```python setup.py develop```  
6. test everything - run usage in debug mode 


## usage
1. run gazebo - ```gazebo --world /home/user/projects/gazebo_visual_united/worlds/iris_arducopter_runway.world --verbose```
2. run sitl -  ```sim_vehicle.py -v ArduCopter -f gazebo-iris --map``` 
3. start gazebo_visual_united  - ```python entry_point.py```
4. [Optional] run a mission - ```python mission_basic.py --connect 127.0.0.1:14550```