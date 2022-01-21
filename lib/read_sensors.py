from picarx_improved import Picarx
while True:
    px = Picarx()
    r=px.ir_sensors.read()
    print(r)