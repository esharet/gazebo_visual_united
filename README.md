# gazebo_visual_united

## installation 
1. clone the project into ~/projects directory 
2. [gazebo installation](http://gazebosim.org/tutorials?tut=install_ubuntu)
   1. after installation run ```source /usr/share/gazebo-11/setup.py```
   2. add these lines to your .bashrc:

      ```export GAZEBO_MODEL_PATH=~/projects/gazebo_visual_united/models:${GAZEBO_MODEL_PATH}```
      ```export   =~/projects/gazebo_visual_united/worlds:${GAZEBO_RESOURCE_PATH}```
   3. test gazebo with the world - ```gazebo --world /home/user/projects/gazebo_visual_united/worlds/iris_arducopter_runway.world --verbose```
   4. you should expect error of failed plugin   
3. sitl installation
   1. sitl check
   2. gazebo and sitl check   
4. install the project  
   1. python3 -m venv venv
   2. in the venv - 
      1. ``` python3 -m pip --upgrade pip setuptools wheel```
      2. ```pip install -r requirements```
   3. generating the messages - 
      1. in the gazebo_unity_messages dir - ```protoc -I=proto --python_out=py_msgs proto/*```
   4. setup - 
      1. in the project root dir - ```python setup.py develop```  
4. test everything - run usage in debug mode 


## usage
1. run gazebo 
2. run sitl 
3. 