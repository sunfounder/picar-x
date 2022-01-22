from picarx_improved import Picarx
px = Picarx()
while True:
    r=px.ir_sensors.read()
    print(r)
