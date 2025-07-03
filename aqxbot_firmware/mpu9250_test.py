#!/usr/bin/env python3
import socket
import json
import time
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

# Setup UDP
UDP_IP = "192.168.1.102"  # Replace with the IP of your ROS machine
UDP_PORT = 8102
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Setup MPU9250
mpu = MPU9250(
    address_ak=AK8963_ADDRESS,
    address_mpu_master=MPU9050_ADDRESS_68,
    address_mpu_slave=None,
    bus=1,
    gfs=GFS_250,
    afs=AFS_2G,
    mfs=AK8963_BIT_16,
    mode=AK8963_MODE_C100HZ
)

# mpu.calibrate()  # optional
mpu.configure()
print('imu data transmission started')
try:
    while True:
        ax, ay, az = mpu.readAccelerometerMaster()
        gx, gy, gz = mpu.readGyroscopeMaster()
        mx, my, mz = mpu.readMagnetometerMaster()
        temp = mpu.readTemperatureMaster()

        imu_data = {
            "accel": [ax, ay, az],
            "gyro": [gx, gy, gz],
            "mag": [mx, my, mz],
            "temp": temp
        }

        sock.sendto(json.dumps(imu_data).encode(), (UDP_IP, UDP_PORT))
        #print("Sent:", imu_data)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopped by user")
except Exception as e:
    print("Error:", e)
