import threading
import socket
import time
import json
from picarx import Picarx
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
from rplidar import RPLidar

# ========== CONFIGURATION ==========
# UDP config
PI_IP = "192.168.1.102"  # IP of ROS2 machine

# Ports
MOTION_PORT = 8100
MPU_PORT = 8102
LIDAR_PORT = 8101

# Lidar
LIDAR_SERIAL = '/dev/ttyUSB0'

# ====================================

# Setup PiCar-X
px = Picarx()

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
mpu.configure()

# Setup UDP sockets
motion_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
motion_sock.bind(("0.0.0.0", MOTION_PORT))
motion_sock.setblocking(False)

mpu_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
lidar_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# ========== THREAD FUNCTIONS ==========

def motion_thread():
    print(f"[MOTION] Listening for UDP commands on port {MOTION_PORT}")
    last_r_vel = None
    last_l_vel = None
    try:
        while True:
            try:
                data, addr = motion_sock.recvfrom(128)
                message = data.decode('utf-8')

                r_vel, l_vel = parse_motor_command(message)
                                # Only print if command changed
                if r_vel != last_r_vel or l_vel != last_l_vel:
                    print(f"[MOTION] Received: {message}")
                    print(f"[MOTION] Parsed - Right: {r_vel}, Left: {l_vel}")
                    last_r_vel = r_vel
                    last_l_vel = l_vel

                px.set_motor_speed(1, int(l_vel))  # left motor
                px.set_motor_speed(2, int(r_vel))  # right motor


            except BlockingIOError:
                pass
            except Exception as e:
                print(f"[MOTION ERROR] {e}")
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("[MOTION] Stopped.")
    finally:
        px.stop()


def mpu_thread():
    print(f"[MPU] Starting IMU stream to {PI_IP}:{MPU_PORT}")
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

            mpu_sock.sendto(json.dumps(imu_data).encode(), (PI_IP, MPU_PORT))
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("[MPU] Stopped by user")
    except Exception as e:
        print("[MPU ERROR]", e)


def lidar_thread():
    print(f"[LIDAR] Starting LIDAR stream to {PI_IP}:{LIDAR_PORT}")
    try:
        lidar = RPLidar(LIDAR_SERIAL)
        for scan in lidar.iter_scans():
            udp_data = [{'angle': meas[1], 'distance': meas[2]} for meas in scan]
            payload = json.dumps(udp_data)
            lidar_sock.sendto(payload.encode(), (PI_IP, LIDAR_PORT))
    except KeyboardInterrupt:
        print("[LIDAR] Stopped by user")
    except Exception as e:
        print("[LIDAR ERROR]", e)
    finally:
        try:
            lidar.stop()
            lidar.disconnect()
            print("[LIDAR] Cleaned up.")
        except:
            pass


# ========== UTILITY FUNCTION ==========
def parse_motor_command(message: str):
    right_velocity = 0.0
    left_velocity = 0.0
    print(f"[DEBUG] Parsing message: '{message}'")
    try:
        for token in message.strip().split(','):
            if len(token) < 3:
                continue
            wheel = token[0]  # 'r' or 'l'
            sign = token[1]   # 'p' or 'n'
            value = float(token[2:])
            value = value if sign == 'p' else -value

            if wheel == 'r':
                right_velocity = value
            elif wheel == 'l':
                left_velocity = value
    except Exception as e:
        print(f"[PARSE ERROR] {e}")
    return right_velocity, left_velocity

# ========== MAIN ==========
if __name__ == '__main__':
    threads = []

    t1 = threading.Thread(target=motion_thread, daemon=True)
    t2 = threading.Thread(target=mpu_thread, daemon=True)
    t3 = threading.Thread(target=lidar_thread, daemon=True)

    threads.extend([t1, t2, t3])

    for t in threads:
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down main thread.")
        px.stop()
        motion_sock.close()
        mpu_sock.close()
        lidar_sock.close()

def mpu_thread():
    print(f"[MPU] Starting IMU stream to {PI_IP}:{MPU_PORT}")
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

            mpu_sock.sendto(json.dumps(imu_data).encode(), (PI_IP, MPU_PORT))
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("[MPU] Stopped by user")
    except Exception as e:
        print("[MPU ERROR]", e)


def lidar_thread():
    print(f"[LIDAR] Starting LIDAR stream to {PI_IP}:{LIDAR_PORT}")
    try:
        lidar = RPLidar(LIDAR_SERIAL)
        for scan in lidar.iter_scans():
            udp_data = [{'angle': meas[1], 'distance': meas[2]} for meas in scan]
            payload = json.dumps(udp_data)
            lidar_sock.sendto(payload.encode(), (PI_IP, LIDAR_PORT))
    except KeyboardInterrupt:
        print("[LIDAR] Stopped by user")
    except Exception as e:
        print("[LIDAR ERROR]", e)
    finally:
        try:
            lidar.stop()
            lidar.disconnect()
            print("[LIDAR] Cleaned up.")
        except:
            pass


# ========== UTILITY FUNCTION ==========
def parse_motor_command(message: str):
    right_velocity = 0.0
    left_velocity = 0.0
    try:
        for token in message.strip().split(','):
            if len(token) < 3:
                continue
            wheel = token[0]  # 'r' or 'l'
            sign = token[1]   # 'p' or 'n'
            value = float(token[2:])
            value = value if sign == 'p' else -value

            if wheel == 'r':
                right_velocity = value
            elif wheel == 'l':
                left_velocity = value
    except Exception as e:
        print(f"[PARSE ERROR] {e}")
    return right_velocity, left_velocity

# ========== MAIN ==========
if __name__ == '__main__':
    threads = []

    t1 = threading.Thread(target=motion_thread, daemon=True)
    t2 = threading.Thread(target=mpu_thread, daemon=True)
    t3 = threading.Thread(target=lidar_thread, daemon=True)

    threads.extend([t1, t2, t3])

    for t in threads:
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down main thread.")
        px.stop()
        motion_sock.close()
        mpu_sock.close()
        lidar_sock.close()
