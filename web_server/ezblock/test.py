from ezblock.sensorkit import Sensorkit
import time
while(True):
    print(Sensorkit.dht11_read.result[0,1])
    time.sleep(1)




