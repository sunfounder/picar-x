from picarx import Picarx


if __name__=='__main__':
  try:
    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2']) 
    px_power = 10
    while True:
        gm_val_list = px.get_grayscale_data()
        print("gm_val_list:",gm_val_list)
        gm_status = px.get_line_status(gm_val_list)
        print("gm_status:",gm_status)

        if gm_status == 'forward':
            print(1)
            px.forward(px_power) 

        elif gm_status == 'left':
            px.set_dir_servo_angle(12)
            px.forward(px_power) 

        elif gm_status == 'right':
            px.set_dir_servo_angle(-12)
            px.forward(px_power) 
        else:
            px.set_dir_servo_angle(0)
            px.stop()
  finally:
      px.stop()
