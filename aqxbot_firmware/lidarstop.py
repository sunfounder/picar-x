from rplidar import RPLidar

# === CONFIG ===
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(PORT_NAME)
    
lidar.stop()