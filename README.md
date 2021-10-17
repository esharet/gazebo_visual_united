# gazebo_visual_united

## installation 
1. gazebo installation 
    1. gazebo check 
    2. add these lines to your ~/.bashrc:
       ```
       echo 'export GAZEBO_MODEL_PATH=~/projects/gazebo_visual_united/models:${GAZEBO_MODEL_PATH}' >> ~/.bashrc
       echo 'export GAZEBO_RESOURCE_PATH=~/projects/gazebo_visual_united/worlds:${GAZEBO_RESOURCE_PATH}' >> ~/.bashrc
       echo 'export GAZEBO_PLUGIN_PATH=~/apm/gazebo_visual_united/build:${GAZEBO_PLUGIN_PATH}' >> ~/.bashrc
       source ~/.bashrc
       ```

    3. compile the plugins:
       ```
       cd build
       cmake ..
       make
       sudo make install
       ```


2. sitl installation
   1. sitl check
   2. gazebo and sitl check   
3. clone the project 
4. install the project  
   1. python3 -m venv venv
   2. in the venv - 
      1. ``` python3 -m pip --upgrade pip setuptools wheel```
      2. ```pip install -r requirements```
   3. generating the messages - 
      1. in the project root dir - ```protoc -I=proto --python_out=msgs proto/*```
5. test everything - run usage in debug mode 


## usage
1. run gazebo 
2. run sitl 
3. 