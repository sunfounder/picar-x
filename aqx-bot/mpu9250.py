from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
import time

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

#mpu.calibrate()
mpu.configure()

try:
    while True:
        ax, ay, az = mpu.readAccelerometerMaster()
        gx, gy, gz = mpu.readGyroscopeMaster()
        mx, my, mz = mpu.readMagnetometerMaster()
        temp = mpu.readTemperatureMaster()

        print(f"Accel (g): ({ax:.2f}, {ay:.2f}, {az:.2f})")
        print(f"Gyro  (s): ({gx:.2f}, {gy:.2f}, {gz:.2f})")
        print(f"Mag   (T): ({mx:.2f}, {my:.2f}, {mz:.2f})")
        print(f"Temp  (C): {temp:.2f}")
        print("------")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program stopped by user")

except Exception as e:
    print(f"Error: {e}")

