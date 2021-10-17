from setuptools import setup, find_packages

package_name = 'gazebo_unity_messages'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(where=package_name),
    install_requires=['protobuf' ],
    zip_safe=True,
    maintainer='user',
    maintainer_email='es@int.com',
    description='TODO: Package description',
    license='TODO: License declaration',
 
)