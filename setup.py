from setuptools import setup, find_packages


setup(
    name='gazebo_unity_package',
    version='1.0.0',
    packages=['gazebo_unity_messages', 'gazebo_visual_united'],
    install_requires=['protobuf' ],
    zip_safe=True,
    maintainer='user',
    maintainer_email='es@int.com',
    description='TODO: Package description',
    license='TODO: License declaration',
 
)