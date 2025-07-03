#!/usr/bin/env python3
'''Reads RPLidar and sends angle/distance data over UDP'''

from rplidar import RPLidar
import socket
import json

# === CONFIG ===
PORT_NAME = '/dev/ttyUSB0'
UDP_IP = '192.168.1.102'   # Replace with your ROS Pi IP
UDP_PORT = 8101

# === Setup UDP Socket ===
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def run():
    lidar = RPLidar(PORT_NAME)
    iterator = lidar.iter_scans()

    print(f"[INFO] Sending LIDAR data to {UDP_IP}:{UDP_PORT}")
    try:
        for scan in iterator:
            udp_data = [{'angle': meas[1], 'distance': meas[2]} for meas in scan]
            payload = json.dumps(udp_data)
            sock.sendto(payload.encode(), (UDP_IP, UDP_PORT))
            #print(f"[INFO] Sent {len(udp_data)} points")
    except KeyboardInterrupt:
        print("[INFO] Stopped by user")
    finally:
        lidar.stop()
        print("[INFO] LIDAR stopped and disconnected")

if __name__ == '__main__':
    run()
