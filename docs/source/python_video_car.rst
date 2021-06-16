Video Car
==========================================

Now we can play in combination with :ref:`Computer Vision` and :ref:`Let PiCar-X Move` .

Let's observe the world from the first point of view of PiCar-X! Adjust the speed with O and P of keyboard and the moving direction with WSAD.

**code**

.. code-block:: python
    
    import sys
    sys.path.append(r'/home/pi/picar-x/lib')

    from utils import reset_mcu
    reset_mcu()
    from picarx import Picarx
    from utils import run_command
    import datetime

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import numpy as np

    camera = PiCamera()
    camera.resolution = (640,480)
    camera.framerate = 24
    camera.image_effect = "none"  #"none","negative","solarize","emboss","posterise","cartoon",
    rawCapture = PiRGBArray(camera, size=camera.resolution)  

    power_val = 0
    px = Picarx()

    try:
        while True:
            for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):# use_video_port=True
                img = frame.array
                cv2.imshow("video", img)   
            
                k = cv2.waitKey(1) & 0xFF
                if k == 27:
                    camera.close()
                    continue
                elif k == ord('o'):
                    if power_val <=90:
                        power_val += 10
                        print("power_val:",power_val)  
                elif k == ord('p'):
                    if power_val >=10:
                        power_val -= 10
                        print("power_val:",power_val) 
                elif k == ord('w'):
                    # print("w:",)
                    px.set_dir_servo_angle(0)
                    px.forward(power_val)
                elif k == ord('a'):
                    px.set_dir_servo_angle(-30) 
                    px.forward(power_val)
                elif k == ord('s'):
                    px.set_dir_servo_angle(0) 
                    px.backward(power_val)
                elif k == ord('d'):
                    px.set_dir_servo_angle(30) 
                    px.forward(power_val)
                elif k == ord('f'):    
                    px.stop()  

                elif k == ord('t'):  
                    camera.close()
                    break
                rawCapture.truncate(0)

            print("take a photo wait...")
            picture_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            picture_path = '/home/pi/Pictures/' + picture_time + '.jpg'

            a_t = "sudo raspistill -t 250  -w 2592 -h 1944 " + " -o " + picture_path

            print(a_t)
            run_command(a_t)

            # Vilib.shuttle_button() 
            camera = PiCamera()
            camera.resolution = (640,480)
            camera.framerate = 24
            camera.image_effect = "none"  #"none","negative","solarize","emboss","posterise","cartoon",
            rawCapture = PiRGBArray(camera, size=camera.resolution)  
    finally:
        px.stop()
        camera.close()


**How it works?** 

Most of this code is described in :ref:`Computer Vision` and :ref:`Let PiCar-X Move` .

You also need to learn about the following.

.. code-block:: python

    k = cv2.waitKey(1) & 0xFF

``waitKey()`` is a function of OpenCV waiting for key press events, and it is also the only way to get and process events in HighGUI. This function will only work when at least one HighGUI window is created and it is in an active state.

* `High-level GUI <https://docs.opencv.org/3.4/d7/dfc/group__highgui.html>`_
* `waitKey - OpenCV <https://docs.opencv.org/3.4/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7>`_

.. code-block:: python

    print("take a photo wait...")
    picture_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    picture_path = '/home/pi/Pictures/' + picture_time + '.jpg'

    a_t = "sudo raspistill -t 250  -w 2592 -h 1944 " + " -o " + picture_path

    print(a_t)
    run_command(a_t)

The effect of these lines of codes is to capture static photos in the tool of command line with Raspberry Pi camera module.
These codes are outside the main loop, and only when OpenCV receives that the **T** key of the keyboard is pressed will it jump out of the loop and execute these codes.

* `raspistill <https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md>`_