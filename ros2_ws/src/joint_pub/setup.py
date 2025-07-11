from setuptools import find_packages, setup

package_name = 'joint_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ishihara',
    maintainer_email='ishikortakkun@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sine_pub = joint_pub.sin_pub:main',
            'play_trajectory = joint_pub.play_trajectory:main',
        ],
    },
)
