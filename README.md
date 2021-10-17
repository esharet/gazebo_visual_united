# gazebo_visual_united

## installation 
1. gazebo installation 
    1. gazebo check 
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